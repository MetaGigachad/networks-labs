.PHONY: build
build:
	docker build -t find-mtu .

.PHONY: run
run:
	docker run --rm --cap-add=NET_RAW find-mtu $(HOST)

