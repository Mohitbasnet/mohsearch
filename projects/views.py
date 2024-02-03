from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project,Tag
from django.contrib import messages
from .forms import ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required
from .utils import searchProjects,paginateProjects
from django.views import View
from django.utils.decorators import method_decorator
# Create your views here.

def projects(request):
    projects, search_query = searchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 6)

    context = {'projects': projects,
               'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'projects/projects.html', context)



# def project(request, pk):
#     projectObj = Project.objects.get(id = pk)
#     form = ReviewForm()
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         review = form.save(commit = False)
#         review.project = projectObj
#         review.owner  = request.user.profile
#         review.save()
#         projectObj.getVoteCount
#         messages.success(request, 'your review is successfully submitted!')
#         return redirect('project',pk = projectObj.id)
#     return render(request, "projects/single-project.html", {'project': projectObj,'form':form})

# Class Based view for project

class ProjectView(View):
    template_name = "projects/single-project.html"
    def get(self, request,pk):
        projectObj = Project.objects.get(id = pk)
        form = ReviewForm()
        return render(request, self.template_name, {'project': projectObj, 'form': form})
    def post(self, request, pk):
         projectObj = Project.objects.get(id=pk)
         form = ReviewForm(request.POST)
         if form.is_valid():
            review = form.save(commit = False)
            review.project = projectObj
            review.owner  = request.user.profile
            review.save()
            projectObj.getVoteCount()
            messages.success(request, 'Your review is successfully submitted!')
            return redirect('project', pk=projectObj.id)
         return render(request, self.template_name,{'project':projectObj, 'form': form} )









 
# @login_required(login_url = "login")
# def createProject(request):
#     profile = request.user.profile
#     form = ProjectForm()
#     if request.method == 'POST':
#         newtags  = request.POST.get('newtags').replace(',', " ").split()
#         form = ProjectForm(request.POST , request.FILES)
#         if form.is_valid():
#             project =  form.save(commit= False)
#             project.owner =  profile
#             project.save()
#             for tag in newtags:
#                 tag, created = Tag.objects.get_or_create(name = tag)
#                 project.tags.add(tag)
#             return redirect('account')
#     context = {"form": form}
#     return render(request,"projects/project_form.html", context)




@method_decorator(login_required, name='dispatch')
class CreateProjectView(View):
    template_name = "projects/project_form.html"
    def get(self, request):
        form = ProjectForm()   # display form
        context = {'form': form}
        return render(request,self.template_name, context)
    
    def post(self, request):
        form = ProjectForm(request.POST, request.FILES)  # handle the project form and project creation
        if form.is_valid():
            project = form.save(commit =False)
            project.owner = self.request.user.profile
            project.save()

            newtags = self.request.POST.get('newtags').replace(',', " ").split()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

            return redirect('account')
        else:
            context = {"form": form}
            return render(request, self.template_name, context)
        



@login_required(login_url = "login")
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance = project)
    if request.method == 'POST':
        newtags  = request.POST.get('newtags').replace(',', " ").split()
        
        form = ProjectForm(request.POST, request.FILES, instance = project)
        if form.is_valid():
            
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name = tag)
                project.tags.add(tag)
            return redirect('account')
    context = {"form": form,
          'project':project}
    return render(request,"projects/project_form.html", context)

@login_required(login_url = "login")
def deleteProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)

    if request.method =='POST':
        project.delete()
        return redirect("account")
    context = {'object':project}
    return render(request,"delete_template.html", context)