from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from json import loads


@method_decorator(csrf_exempt, name='dispatch')
class AdditionView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)

        n1 = form_data.get("num1")
        n2 = form_data.get("num2")

        result = n1 + n2

        data = {
            "sum": result
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class SubtractionView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)

        n1 = form_data.get("num1")
        n2 = form_data.get("num2")

        result = n1 - n2

        return JsonResponse({
            "message": "substraction api",
            "difference": result
        })


@method_decorator(csrf_exempt, name='dispatch')
class MultiplicationView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)

        n1 = form_data.get("num1")
        n2 = form_data.get("num2")

        result = n1 * n2

        return JsonResponse({
            "product": result
        })


@method_decorator(csrf_exempt, name='dispatch')
class DivisionView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)

        n1 = form_data.get("num1")
        n2 = form_data.get("num2")

        result = n1 / n2

        return JsonResponse({
            "division": result
        })


@method_decorator(csrf_exempt, name='dispatch')
class ModulusView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)

        n1 = form_data.get("num1")
        n2 = form_data.get("num2")

        result = n1 % n2

        return JsonResponse({
            "modulus": result
        })

@method_decorator(csrf_exempt, name='dispatch')
class BMIView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)

        height = form_data.get("height")
        weight = form_data.get("weight")

        height = height / 100

        BMI = weight / (height**2)

        return JsonResponse({
            "bmi": BMI
        })


@method_decorator(csrf_exempt, name='dispatch')
class AgeView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)

        birth_year = form_data.get("birth_year")
        current_year = form_data.get("current_year")

        age = current_year - birth_year

        return JsonResponse({
            "age": age
        })
        


@method_decorator(csrf_exempt, name='dispatch')
class PercentageView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)

        obtained_mark = form_data.get("obtained_mark")
        total_mark = form_data.get("total_mark")

        percentage = obtained_mark / total_mark * 100

        return JsonResponse({
            "percentage": percentage
        })      
        


@method_decorator(csrf_exempt, name='dispatch')
class AreaView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)

        length = form_data.get("length")
        width = form_data.get("width")

        area = length * width

        return JsonResponse({
            "area": area
        })

@method_decorator(csrf_exempt, name='dispatch')
class InterstView(View):
    def post (self, request):
        request_body = request.body
        form_data = loads(request_body)

        principal = form_data.get("principal")
        rate = form_data.get("rate")
        time = form_data.get("time")

        simple_intrest = (principal * rate * time) / 100
        return JsonResponse({
            "area": area
        })
