# def printAllSublists(nums):
#     for i in range(len(nums)):
#         total=0
#         for j in range(i,len(nums)):
#             total+=nums[j]
#             if total==0:
#                 print('Sublist',(i, j))
# if __name__ == '__main__':
#     nums=[3,4,-7,3,1,3,1,-4,-2,-2]
#     printAllSublists(nums)
#
#
#
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
#
#
# class Tasklist(APIView):
#     def get(self,request):
#         tasks=Task.objects.all()
#         serializer=Taskserializer(tasks,many=True)
#         return Response(serializer.data)
#     def get(self,request):
#         serializer=Taskserializer(tasks,many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_204_NO_CONTENT)
#
#
# class TaskDetail(APIView):
#     def get(self,request,pk):
#         tasks=Task.objects.get(id=pk)
#         serializer=Taskserializer(tasks)
#         return Response(serializer.data)
#     def put(self,request,pk):
#         tasks=Task.objects.get(id=pk)
#         serializer=Taskserializer(tasks,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#     def delete(self,request,pk):
#         tasks=Task.objects.get(id=pk)
#         tasks.delete()
#         return Response()
#
#
# @api_view(["GET"])
# def tasklist(request):
#     tasks = Task.objects.all()
#     serializer = Taskserializer(tasks, many=True)
#     return Response(serializer.data)
#
# @api_view(["GET"])
# def taskDetail(request,pk):
#     tasks = Task.objects.get(id=pk)
#     serializer = Taskserializer(tasks, many=False)
#     return Response(serializer.data)
#
# @api_view(["POST"])
# def taskCreate(request):
#     serializer = Taskserializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
# @api_view(["POST"])
# def taskCreate(request,pk):
#     tasks = Task.objects.get(id=pk)
#     serializer = Taskserializer(instance=Task,data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#



#
# {-5, 5, 3, 5}
# {3, 5}
# {5, 3}

#
# def merge_sort(alist,start,end):
#     if end - start > 1:
#         mid = (start + end) // 2
#         merge_sort(alist, start, mid)
#         merge_sort(alist, mid, end)
#         merge_list(alist, start, mid, end)
#
# def merge_list(alist,start,mid,end):
#     left=alist[start:mid]
#     right=alist[mid:end]
#     k=start
#     i=0
#     j=0
#     while (start+i<mid and mid+j<end):
#         if (left[i]<right[j]):
#             alist[k]=left[i]
#             i=i+1
#         else:
#             alist[k]=right[j]
#             j=j+1
#         k=k+1
#     if start+i<mid:
#         while k<end:
#             alist[k] = left[i]
#             i = i + 1
#             k = k + 1
#     else:
#         while k < end:
#             alist[k] = right[j]
#             j = j + 1
#             k = k + 1
#
# alist = input('Enter the list of numbers: ').split()
# alist = [int(x) for x in alist]
# merge_sort(alist, 0, len(alist))
# print('Sorted list: ', end='')
# print(alist)



