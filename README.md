# Docker Configuration for the DDC Server

## Overview
The [DDC Server](https://github.com/sassoftware/sas-visualanalytics-thirdpartyvisualizations/tree/master/ddc-server) is a lightweight deployment which provides a range of third-party visualizations to be accessed from within SAS Visual Analytics.  This deployment, served over Kubernetes or as a Docker image, is based on a Flask web application.  This repository provides you the Flask web application and a Dockerfile, which you can use to build your own DDC Server.


## Instructions

1. Modify the Flask application within the [ddc](./ddc) as needed.
2. Create a Docker image using the attached [Dockerfile](./Dockerfile).
```
docker build . -t {{YOUR_DOCKER_NAME}}
```
3. Push the Docker image to a repository of your choice.
```
docker tag app {{YOUR_CR}}/{{CONTAINER_NAME}}:{{TAG}}
docker push {{YOUR_CR}}/{{CONTAINER_NAME}}:{{TAG}}
```
4. Use the attached [deployment file](./deploy-ddc-server.yaml) to deploy on to a Kubernetes cluster.  Make sure to assign values to the placeholder variables ( {{variable}} ) within this file.

Enjoy!


## Support and Contact

For questions regarding the Docker and application, feel free to get in touch with sundaresh.sankaran@sas.com, or @github.com/SundareshSankaran.

