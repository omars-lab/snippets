SHELL := /bin/bash
ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

ENCRYPTED_DIR := ${ROOT_DIR}/src/main/resources/encrypted
DECRYPTED_DIR := ${ROOT_DIR}/src/main/resources/decrypted
PASSWORD := $(shell read -sp "Password: " PASSWORD; echo "$${PASSWORD}")

encrypt:
	ls -1 ${DECRYPTED_DIR} | \
	  xargs -n 1 bash -c \
	    'PASSWORD=${PASSWORD} openssl enc -aes-256-cbc -pass 'env:PASSWORD' -in "${DECRYPTED_DIR}/$${0}" -out "${ENCRYPTED_DIR}/$${0}.dat"'

decrypt:
	ls -1 ${ENCRYPTED_DIR} | \
	  xargs -n 1 bash -c \
	   'PASSWORD=${PASSWORD} openssl enc -aes-256-cbc -d -pass 'env:PASSWORD' -in "${ENCRYPTED_DIR}/$${0}" > "${DECRYPTED_DIR}/$${0%.???}"'

