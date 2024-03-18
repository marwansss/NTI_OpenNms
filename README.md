OpenNMS Project Deployment
This repository contains the deployment configuration for our OpenNMS project, which utilizes a PostgreSQL database. The deployment is orchestrated into two containers: one for the OpenNMS service and the other for the PostgreSQL database service.

Overview
The deployment follows containerization best practices and ensures efficient resource utilization.

Containerization
We have sourced container images from Docker Hub:

OpenNMS Service: Utilizing opennms/horizon image.
Database Service: Utilizing postgres:15 image.
Configuration
A Docker Compose file has been meticulously configured to define container specifications, network settings, and environment variables.

Enhancements
Persistence Volume: Implemented for PostgreSQL data backups to ensure data integrity.
Port Mapping: Configured to facilitate external access to the OpenNMS application from the host machine.
Future Plans
We are preparing to orchestrate our deployment using Kubernetes for advanced container management, scalability, and automation, aligning with industry standards.

Contributing
Feel free to contribute by opening a pull request or raising an issue for any improvements or suggestions.
