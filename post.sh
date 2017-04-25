#!/bin/bash
curl -X PUT -d title="$1" -d text="$2" -d key="SuperSexySecret2FAKey" localhost:8080/new
