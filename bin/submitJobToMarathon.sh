#!/bin/bash

curl -X PUT -H "Content-Type: application/json" localhost:8080/v2/apps/ubuntu -d@../lib/rainbowroad.json
