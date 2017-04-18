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
# Migrate
# -------------------------------------------------------

${VENV}/bin/python manage.py makemigrations
${VENV}/bin/python manage.py migrate

