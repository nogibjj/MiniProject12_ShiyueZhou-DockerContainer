# Define the image name
IMAGE_NAME = container_demo
DOCKER_ID_USER = cynthiashiyue

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Stop any running container using port 8080
stop_conflict:
	@if lsof -i :8080; then \
		echo "Port 8080 is in use. Stopping conflicting containers..."; \
		docker ps -q --filter "ancestor=$(IMAGE_NAME)" | xargs -r docker stop; \
		docker ps -q --filter "publish=8080" | xargs -r docker stop; \
	fi

# Run the Docker container
run: stop_conflict
	docker run -p 8080:8080 $(IMAGE_NAME)

# Remove the Docker image
clean:
	docker rmi $(IMAGE_NAME)

image_show:
	docker images

container_show:
	docker ps

push:
	docker login
	docker tag $(IMAGE_NAME) $(DOCKER_ID_USER)/$(IMAGE_NAME)
	docker push $(DOCKER_ID_USER)/$(IMAGE_NAME):latest

login:
	docker login -u ${DOCKER_ID_USER}

pull: 
	docker pull ${DOCKER_ID_USER}/$(IMAGE_NAME)


all: build stop_conflict run push pull


