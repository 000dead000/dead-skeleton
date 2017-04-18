#!/bin/bash

# -------------------------------------------------------
# Instance directory
# -------------------------------------------------------

DEPLOY_PATH=$( cd "$(dirname "$0")" ; pwd -P )
SCRIPTS_PATH=$(dirname "$DEPLOY_PATH")

INSTANCE=$(dirname "$SCRIPTS_PATH")

# -------------------------------------------------------
# Virtualenv directory
# -------------------------------------------------------

INSTANCE_NAME=$(basename "$INSTANCE")
VENV="$WORKON_HOME/$INSTANCE_NAME"

if [ ! -d "$VENV" ]
then
    echo "No existe una virtualenv para esta instancia"
    exit 1
fi

# -------------------------------------------------------
# Apache
# -------------------------------------------------------

APACHE_SITE_FILE="$INSTANCE_NAME.conf"

# -------------------------------------------------------
# Environment
# -------------------------------------------------------

RUNNING_ENVIRONMENT_DEV="dev"
RUNNING_ENVIRONMENT_TEST="test"
RUNNING_ENVIRONMENT_PRODUCTION="production"

if [ -z "$1" ]
then
    RUNNING_ENVIRONMENT=$RUNNING_ENVIRONMENT_DEV
else
    RUNNING_ENVIRONMENT=$1
fi

# -------------------------------------------------------
# Goto instance dir
# -------------------------------------------------------

cd $INSTANCE

# -------------------------------------------------------
# Update code
# -------------------------------------------------------

if [ "$RUNNING_ENVIRONMENT" = "$RUNNING_ENVIRONMENT_TEST" ] || [ "$RUNNING_ENVIRONMENT" = "$RUNNING_ENVIRONMENT_PRODUCTION" ]
then
    git reset --hard
    git pull
fi

# -------------------------------------------------------
# Set running env in custom_settings
# -------------------------------------------------------

if [ "$RUNNING_ENVIRONMENT" = "$RUNNING_ENVIRONMENT_TEST" ]
then
    sed -i 's/RUNNING_ENVIRONMENT = RUNNING_ENVIRONMENT_DEV/RUNNING_ENVIRONMENT = RUNNING_ENVIRONMENT_TEST/g' ${INSTANCE}/conf/custom_settings.py
elif [ "$RUNNING_ENVIRONMENT" = "$RUNNING_ENVIRONMENT_PRODUCTION" ]
then
    sed -i 's/RUNNING_ENVIRONMENT = RUNNING_ENVIRONMENT_DEV/RUNNING_ENVIRONMENT = RUNNING_ENVIRONMENT_PRODUCTION/g' ${INSTANCE}/conf/custom_settings.py
fi

# -------------------------------------------------------
# Install requirements
# -------------------------------------------------------

${VENV}/bin/dead-command.py pip_dependencies

# -------------------------------------------------------
# Set logic link for apache
# -------------------------------------------------------

if [ "$RUNNING_ENVIRONMENT" = "$RUNNING_ENVIRONMENT_TEST" ] || [ "$RUNNING_ENVIRONMENT" = "$RUNNING_ENVIRONMENT_PRODUCTION" ]
then
    ln -sf ${INSTANCE}/scripts/apache/${RUNNING_ENVIRONMENT}.conf /etc/apache2/sites-available/${APACHE_SITE_FILE}
fi

# -------------------------------------------------------
# Migrate
# -------------------------------------------------------

${VENV}/bin/dead-command.py migrate

# -------------------------------------------------------
# Bower
# -------------------------------------------------------

${VENV}/bin/dead-command.py bower_dependencies

# -------------------------------------------------------
# collect static
# -------------------------------------------------------

if [ "$RUNNING_ENVIRONMENT" = "$RUNNING_ENVIRONMENT_TEST" ] || [ "$RUNNING_ENVIRONMENT" = "$RUNNING_ENVIRONMENT_PRODUCTION" ]
then
    ${VENV}/bin/python manage.py collectstatic --no-input
fi

# -------------------------------------------------------
# Change permissions
# -------------------------------------------------------

if [ "$RUNNING_ENVIRONMENT" = "$RUNNING_ENVIRONMENT_TEST" ] || [ "$RUNNING_ENVIRONMENT" = "$RUNNING_ENVIRONMENT_PRODUCTION" ]
then
    chown -R www-data.www-data ${INSTANCE}
    chmod -R 755 ${INSTANCE}
    service apache2 reload
fi
