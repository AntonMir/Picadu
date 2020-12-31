import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader


database = [

]


def index(request):
  return render(request, 'index.html')






def user(request):
  if request.method == 'GET':

    some_data = {
      'name': 'Raghav',
      'location': 'India',
      'isActive': False,
      'count': 28
    }

    json_data = json.dumps(some_data)
    # return HttpResponse(json_data, status=200, content_type='application/json')
    return JsonResponse(json_data, safe=False)











  elif request.method == 'POST': 
    data = json.loads(request.body)
    print(data)
    database.append(data)
    print('POSTdatabase', database)
    return HttpResponse(status=201)

  elif request.method == 'PUT':
    data = json.loads(request.body)
    print(data)

    print('PUTdatabase', database)    
    return HttpResponse(status=200)

  elif request.method == 'DELITE':
    return HttpResponse(status=204)
  

 









#   # template = loader.get_template('index.html')
#   # if request.method == "GET":
#   #    # получаем шаблон
#   #   # передаем, что будет передано на клиент
#   #   context = {
#   #     'test': [1,2,3,4,5,6,7], 
#   #     'context2': {
#   #       'test2': 'test2234634',
#   #     },
#   #   }
#   #   # возвращаем ответ HTTP с нашим отрисованным шаблоном
#   #   return HttpResponse(template.render(context, request))
#   #   # return render(request, 'index.html', test = 123)
#   # elif request.method == 'POST':
#   #   json_data = request.POST.get('test3')
#   #   print('json_data', json_data)
#   #   context = {
#   #     'test': json_data, 
#   #   }
#   #   new_template = template.render(context)
#     # return HttpResponse(new_template, status=201)




# # def my_view(request):
# #   if request.method == "POST":
# #     print('type', type(request.body))
# #     json_data = json.loads(request.body)
# #     print('json_data', json_data)
# #     for object in json_data:
# #       email = object['email']
# #       print(email)
# #     return HttpResponse(status=201)
# #   return HttpResponse(status=200)







