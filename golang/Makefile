COLOR := $(shell git rev-parse HEAD | cut -c 1-6)
DOCKER_IMAGE ?= alexlovelltroy/rainbow-mnemonic

.PHONY: build
build: rainbow-mnemonic

rainbow-mnemonic: main.go
	go build -o rainbow-mnemonic

.PHONY: image
image:
	@echo Building with color $(COLOR)
	COLOR=$(COLOR) docker build . -t $(DOCKER_IMAGE):$(COLOR) --build-arg COLOR=$(COLOR) -f Dockerfile.golang

.PHONY: push
push: image
	docker push $(DOCKER_IMAGE):$(COLOR)

.PHONY: push-gcloud
push-gcloud: 
	docker tag $(DOCKER_IMAGE):$(COLOR) gcr.io/maas-kube-rainbow/$(DOCKER_IMAGE):$(COLOR)
	gcloud docker -- push gcr.io/maas-kube-rainbow/$(DOCKER_IMAGE):$(COLOR)

.PHONY: submit-gcloud
submit-gcloud: 
	gcloud container builds submit --tag gcr.io/maas-kube-rainbow/$(DOCKER_IMAGE):$(COLOR) .


.PHONY: install
install:
	cat app.yaml | sed s/__COLOR__/$(COLOR)/g | kubectl apply -f -
