PYTHON = python2
VAR_DIR = $(CURDIR)/var
VIRTUAL_ENV = $(VAR_DIR)/ve
PYTHON_BIN = $(VIRTUAL_ENV)/bin
DEPLOY_DIR = $(VAR_DIR)/deploy

pack: cleandeploydir
	mkdir -p $(VAR_DIR)/deploy
	cp -R $(CURDIR)/sqs_auto_scale $(DEPLOY_DIR)
	cp -R $(VIRTUAL_ENV)/lib/python2.7/site-packages/* $(DEPLOY_DIR)
	cp $(CURDIR)/main.py $(DEPLOY_DIR)/
	find $(DEPLOY_DIR) -name "*.pyc" -delete;
	cd $(DEPLOY_DIR) && zip -r9 $(VAR_DIR)/sqs-auto-scale.zip *


deploy: pack
	aws lambda update-function-code \
	--function-name sqs_auto_scale \
	--zip-file fileb://$(VAR_DIR)/sqs-auto-scale.zip \
	--profile default \


firstdeploy: pack
	aws lambda create-function \
	--function-name sqs_auto_scale \
	--zip-file fileb://$(VAR_DIR)/sqs-auto-scale.zip \
	--handler main.lambda_handler \
	--runtime python2.7 \
	--profile default \
	--timeout 10 \
	--memory-size 1024 \
	--role arn:aws:iam::291890047404:role/CloudCustodianLambdaS3PublicObjectAcessRemove

install:
	mkdir -p $(VIRTUAL_ENV)
	virtualenv -p $(PYTHON) --no-site-packages $(VIRTUAL_ENV)
	$(PYTHON_BIN)/pip install --upgrade pip -r requirements.txt

clean:
	rm -Rf $(VAR_DIR)

cleandeploydir:
	rm -Rf $(DEPLOY_DIR)

