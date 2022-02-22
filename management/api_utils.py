from management.models import Files

def get_master_search_dictionary():

    master_dictionary = {
        
    }

    all_files  = Files.objects.all()

    for file in all_files:
        
        pass