# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/helloworld.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16proto/helloworld.proto\x12\x1e\x63om.github.wesleywu.helloworld\"\"\n\x0cHelloRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\"&\n\nHelloReply\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message2q\n\x07Greeter\x12\x66\n\x08SayHello\x12,.com.github.wesleywu.helloworld.HelloRequest\x1a*.com.github.wesleywu.helloworld.HelloReply\"\x00\x42\x0fZ\r./;helloworldb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.helloworld_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\r./;helloworld'
  _globals['_HELLOREQUEST']._serialized_start=58
  _globals['_HELLOREQUEST']._serialized_end=92
  _globals['_HELLOREPLY']._serialized_start=94
  _globals['_HELLOREPLY']._serialized_end=132
  _globals['_GREETER']._serialized_start=134
  _globals['_GREETER']._serialized_end=247
# @@protoc_insertion_point(module_scope)
