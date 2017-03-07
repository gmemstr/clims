#!/bin/bash
curl -X PUT -d title="$1" -d text="$2" localhost:8080/new/long
