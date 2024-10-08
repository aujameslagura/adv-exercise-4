from django.contrib import admin
from .models import Tag  # Import your model here

# Register the Tag model
@admin.register(Tag)  # This decorator registers the Tag model with the admin site
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Specify the fields to display in the admin list view
    search_fields = ('name',)  # Enable a search box for the name field
  
    