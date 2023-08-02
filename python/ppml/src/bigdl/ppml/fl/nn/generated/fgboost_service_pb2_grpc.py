# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import fgboost_service_pb2 as fgboost__service__pb2


class FGBoostServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.uploadLabel = channel.unary_unary(
                '/fgboost.FGBoostService/uploadLabel',
                request_serializer=fgboost__service__pb2.UploadLabelRequest.SerializeToString,
                response_deserializer=fgboost__service__pb2.UploadResponse.FromString,
                )
        self.downloadLabel = channel.unary_unary(
                '/fgboost.FGBoostService/downloadLabel',
                request_serializer=fgboost__service__pb2.DownloadLabelRequest.SerializeToString,
                response_deserializer=fgboost__service__pb2.DownloadResponse.FromString,
                )
        self.split = channel.unary_unary(
                '/fgboost.FGBoostService/split',
                request_serializer=fgboost__service__pb2.SplitRequest.SerializeToString,
                response_deserializer=fgboost__service__pb2.SplitResponse.FromString,
                )
        self.register = channel.unary_unary(
                '/fgboost.FGBoostService/register',
                request_serializer=fgboost__service__pb2.RegisterRequest.SerializeToString,
                response_deserializer=fgboost__service__pb2.RegisterResponse.FromString,
                )
        self.uploadTreeLeaf = channel.unary_unary(
                '/fgboost.FGBoostService/uploadTreeLeaf',
                request_serializer=fgboost__service__pb2.UploadTreeLeafRequest.SerializeToString,
                response_deserializer=fgboost__service__pb2.UploadResponse.FromString,
                )
        self.evaluate = channel.unary_unary(
                '/fgboost.FGBoostService/evaluate',
                request_serializer=fgboost__service__pb2.EvaluateRequest.SerializeToString,
                response_deserializer=fgboost__service__pb2.EvaluateResponse.FromString,
                )
        self.predict = channel.unary_unary(
                '/fgboost.FGBoostService/predict',
                request_serializer=fgboost__service__pb2.PredictRequest.SerializeToString,
                response_deserializer=fgboost__service__pb2.PredictResponse.FromString,
                )
        self.saveServerModel = channel.unary_unary(
                '/fgboost.FGBoostService/saveServerModel',
                request_serializer=fgboost__service__pb2.SaveModelRequest.SerializeToString,
                response_deserializer=fgboost__service__pb2.SaveModelResponse.FromString,
                )
        self.loadServerModel = channel.unary_unary(
                '/fgboost.FGBoostService/loadServerModel',
                request_serializer=fgboost__service__pb2.LoadModelRequest.SerializeToString,
                response_deserializer=fgboost__service__pb2.LoadModelResponse.FromString,
                )


class FGBoostServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def uploadLabel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def downloadLabel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def split(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def uploadTreeLeaf(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def evaluate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def predict(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def saveServerModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def loadServerModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FGBoostServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'uploadLabel': grpc.unary_unary_rpc_method_handler(
                    servicer.uploadLabel,
                    request_deserializer=fgboost__service__pb2.UploadLabelRequest.FromString,
                    response_serializer=fgboost__service__pb2.UploadResponse.SerializeToString,
            ),
            'downloadLabel': grpc.unary_unary_rpc_method_handler(
                    servicer.downloadLabel,
                    request_deserializer=fgboost__service__pb2.DownloadLabelRequest.FromString,
                    response_serializer=fgboost__service__pb2.DownloadResponse.SerializeToString,
            ),
            'split': grpc.unary_unary_rpc_method_handler(
                    servicer.split,
                    request_deserializer=fgboost__service__pb2.SplitRequest.FromString,
                    response_serializer=fgboost__service__pb2.SplitResponse.SerializeToString,
            ),
            'register': grpc.unary_unary_rpc_method_handler(
                    servicer.register,
                    request_deserializer=fgboost__service__pb2.RegisterRequest.FromString,
                    response_serializer=fgboost__service__pb2.RegisterResponse.SerializeToString,
            ),
            'uploadTreeLeaf': grpc.unary_unary_rpc_method_handler(
                    servicer.uploadTreeLeaf,
                    request_deserializer=fgboost__service__pb2.UploadTreeLeafRequest.FromString,
                    response_serializer=fgboost__service__pb2.UploadResponse.SerializeToString,
            ),
            'evaluate': grpc.unary_unary_rpc_method_handler(
                    servicer.evaluate,
                    request_deserializer=fgboost__service__pb2.EvaluateRequest.FromString,
                    response_serializer=fgboost__service__pb2.EvaluateResponse.SerializeToString,
            ),
            'predict': grpc.unary_unary_rpc_method_handler(
                    servicer.predict,
                    request_deserializer=fgboost__service__pb2.PredictRequest.FromString,
                    response_serializer=fgboost__service__pb2.PredictResponse.SerializeToString,
            ),
            'saveServerModel': grpc.unary_unary_rpc_method_handler(
                    servicer.saveServerModel,
                    request_deserializer=fgboost__service__pb2.SaveModelRequest.FromString,
                    response_serializer=fgboost__service__pb2.SaveModelResponse.SerializeToString,
            ),
            'loadServerModel': grpc.unary_unary_rpc_method_handler(
                    servicer.loadServerModel,
                    request_deserializer=fgboost__service__pb2.LoadModelRequest.FromString,
                    response_serializer=fgboost__service__pb2.LoadModelResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fgboost.FGBoostService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FGBoostService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def uploadLabel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fgboost.FGBoostService/uploadLabel',
            fgboost__service__pb2.UploadLabelRequest.SerializeToString,
            fgboost__service__pb2.UploadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def downloadLabel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fgboost.FGBoostService/downloadLabel',
            fgboost__service__pb2.DownloadLabelRequest.SerializeToString,
            fgboost__service__pb2.DownloadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def split(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fgboost.FGBoostService/split',
            fgboost__service__pb2.SplitRequest.SerializeToString,
            fgboost__service__pb2.SplitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fgboost.FGBoostService/register',
            fgboost__service__pb2.RegisterRequest.SerializeToString,
            fgboost__service__pb2.RegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def uploadTreeLeaf(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fgboost.FGBoostService/uploadTreeLeaf',
            fgboost__service__pb2.UploadTreeLeafRequest.SerializeToString,
            fgboost__service__pb2.UploadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def evaluate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fgboost.FGBoostService/evaluate',
            fgboost__service__pb2.EvaluateRequest.SerializeToString,
            fgboost__service__pb2.EvaluateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def predict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fgboost.FGBoostService/predict',
            fgboost__service__pb2.PredictRequest.SerializeToString,
            fgboost__service__pb2.PredictResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def saveServerModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fgboost.FGBoostService/saveServerModel',
            fgboost__service__pb2.SaveModelRequest.SerializeToString,
            fgboost__service__pb2.SaveModelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def loadServerModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fgboost.FGBoostService/loadServerModel',
            fgboost__service__pb2.LoadModelRequest.SerializeToString,
            fgboost__service__pb2.LoadModelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)