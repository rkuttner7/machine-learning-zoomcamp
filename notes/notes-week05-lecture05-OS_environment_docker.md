# 5.6 Environment management: Docker


### Notes

* [Search Docker hub](https://hub.docker.com/search?type=image)  
    * Identify low dependency, "slim", [Python image](https://hub.docker.com/_/python) `3.12.12-slim`. 
        * Must be Python version 3.10+ for `pipenv`. 
        * Must match `Pipfile` python_version (currently at "3.12")
    

### **Functions and methods:**  
* `docker run [-flags] [--options] [base image]` - execute any commands on top of the current image  
    * **Example flags**:
        * `-it` - spawn interactive terminal shell  
    * **Example options**:  
        * `--rm` - remove the image after use  
    * **Example entrypoint**:  
        * `--entrypoint=bash` - set initial command to open in terminal (default command at runtime is `python`)  
    * **Example port mapping**:  
        * `-p [host machine port]:[container port]` - publish the port when running the container.  
    * **Example docker run**:
        * `docker run -it --rm --entrypoint=bash python:3.10.19-slim`
        * `docker run -it --rm -p 9696:9696 zoomcamp-test`

* `Dockerfile` - build images automatically from instructions in the Dockerfile.  
    * `FROM` - set the base image for subsequent instructions  
    * `RUN` - execute any commands on top of the current image 
    * `WORKDIR` - set the working directory for any subsequent `ADD`, `COPY`, `CMD`, `ENTRYPOINT`, or `RUN` instructions that follow it in the Dockerfile. Creates directory, if it does not exist.  
    * `COPY` - Copy files or folders from source to the dest path in the image's filesystem.  
        * **Example**: `COPY ["a.txt", "b.txt", "./"]` - copy files {"a.txt", "b.txt"} from source to the working directory in the image.  
    * `EXPOSE` - which ports your application is listening on,
    * `ENTRYPOINT` - 
        * **Examples** : set default executable. (Defaults to Python shell)
            * `["bash"]` - open in terminal
            * `["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]` - 
  
* `docker build -t zoomcamp-test .`
    * `-t` - tag name "zoomcamp-test"  
    * `.` - build from Dockerfile in current directory
  
* `pipenv install --deploy --system` - installs dependencies directly to the system Python instead of a virtual environment, ensuring that the installation fails if the `Pipfile.lock` is out of date.  


### **Futher Reading**  
* [Dockerfile reference | official](https://docs.docker.com/reference/dockerfile) commands you can use in a Dockerfile.  
* [Networking: Port publishing | official Docker](https://docs.docker.com/engine/network/port-publishing/)  