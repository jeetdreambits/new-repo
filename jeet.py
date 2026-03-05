class GithubEvent(models.Model):
    _name = "github.event"
    _description = "GitHub Event"



    
    
    event_type = fields.Char("Event Type")
    repository = fields.Char("Repository")
    author = fields.Char("Author") 
    message = fields.Text("Message")    
    created_at = fields.Datetime("Created At")
  
