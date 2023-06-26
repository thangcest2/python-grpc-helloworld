from concurrent import futures

import grpc
import greeting_pb2
import greeting_pb2_grpc


class Greeter(greeting_pb2_grpc.GreeterServicer):
    def greet(self, request, context):
        print("Got request " + str(request))
        return greeting_pb2.ServerOutput(message='{0} {1}!'.format(request.greeting, request.name))


def server():
    _server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    greeting_pb2_grpc.add_GreeterServicer_to_server(Greeter(), _server)
    _server.add_insecure_port('[::]:50051')
    print("gRPC starting")
    _server.start()
    _server.wait_for_termination()


server()
