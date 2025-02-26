import time
import json
from traceback import format_exc
from django.utils.deprecation import MiddlewareMixin
from utils.logger import write_log


class RequestResponseLoggerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """记录请求开始信息"""
        request.start_time = time.time()
        
        log_data = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'method': request.method,
            'path': request.path,
            'user': request.user.username if request.user.is_authenticated else '匿名',

            # 安全过滤敏感参数
            'params': self.filter_sensitive_data(request.GET),
            'body': self.filter_sensitive_data(request.POST),
            'json': self.filter_sensitive_data(request.json),
            'headers': self.filter_sensitive_headers(request.headers.items()),
        }
        write_log('info', f"Request: {log_data}")

    def process_response(self, request, response):
        """记录响应结束信息"""
        total_time = time.time() - request.start_time
        
        log_data = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'status': response.status_code,
            'length': len(response.content),
            'content': response.content,
            'time_taken': f"{total_time:.2f}s",
            'user': request.user.username if request.user.is_authenticated else '匿名',
        }
        write_log('info', f"Response: {log_data}")
        return response

    def process_exception(self, request, exception):
        """捕获异常并记录"""
        stack_trace = format_exc()
        
        log_data = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'method': request.method,
            'path': request.path,
            'user': request.user.username if request.user.is_authenticated else '匿名',
            'exception': f"{type(exception).__name__}: {str(exception)}",
            'traceback': stack_trace,
            
            # 安全过滤敏感参数
            'params': self.filter_sensitive_data(request.GET),
            'headers': self.filter_sensitive_headers(request.headers.items()),
        }
        write_log('error', f"Exception: {log_data}")
        return None  # 继续异常处理流程

    @staticmethod
    def filter_sensitive_data(params):
        """过滤敏感参数"""
        to_record = {}
        for key in params:
            if key in ['key_name1', 'key_name2']:
                continue
            to_record[key] = params[key]

        return to_record

    @staticmethod
    def filter_sensitive_headers(headers):
        """过滤敏感头部信息"""
        to_record = {}
        for key, value in headers:
            if key in ['Authorization', 'Cookie', 'Set-Cookie']:
                continue
            to_record[key] = value

        return to_record


class JsonMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.content_type == 'application/json' and request.body:
            try:
                request.json = json.loads(request.body.decode('utf-8'))
            except json.JSONDecodeError:
                request.json = {}
        else:
            request.json = {}
        return None
