#!/bin/sh -e


snapcraft clean && SNAPCRAFT_BUILD_ENVIRONMENT_MEMORY=8G snapcraft
