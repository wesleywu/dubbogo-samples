# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

import logging
from dotenv import load_dotenv
import grpc
import os
import sys

sys.path.append('../gen/proto/python')

from helloworld.gen.proto.python import helloworld_pb2
from helloworld.gen.proto.python import helloworld_pb2_grpc


def run():
    load_dotenv()
    try:
        greeter_service_endpoint = os.environ['GREETER_SERVICE_ENDPOINT']
    except KeyError:
        raise 'Environment variable GREETER_SERVICE_ENDPOINT not set'

    print(f'Calling rpc {greeter_service_endpoint} to greet world ...')

    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel(greeter_service_endpoint) as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='Wesley Wu'))
    print('Greeter client received: ' + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()