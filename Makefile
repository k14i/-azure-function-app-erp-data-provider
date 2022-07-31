start:
	func start --python

start-verbose:
	func start --verbose --python

start-debug:
	func start --verbose --python --debug

start-trace:
	func start --verbose --python --debug --trace

start-profile:
	func start --verbose --python --debug --trace --profile

call-post:
	curl -X POST -H "Content-Type: application/json" -d "{}" "http://localhost:7071/api/HttpTrigger-erp-data-provider"
