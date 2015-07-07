# i18n-django-api
Django resful backend to support i18n


##database

page
[id, slug, title]

content
[id, name(unique), page_id]

i18n_content
[id, lang, content_id, content]

page_translation
[id, page_id, lang, title]

## restful api

/api/<lang>/pages/
/api/<lang>/page/<slug>
/api/<lang>/page/<slug>/contents/
/api/<lang>/content/<content_id>

