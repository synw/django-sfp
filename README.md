Django Sfp
==========

Serve flat pages for a Vuejs frontend

* **Fast**: no database hits
* **Safe**: keep the pages in a version control system
* **Friendly**: edit the pages in an IDE
* **Cache**: client-side cache thanks to [Apollo client](https://www.apollographql.com/)

Installation
------------

``pip install django-sfp``

Configuration
-------------

1. Add ``"sfp",`` to your ``INSTALLED_APPS``

2. Declare the graphql schema in settings:

   ```python
   GRAPHENE = {
      'SCHEMA': 'sfp.schema.schema',
   }
   ```

3. Add the graphql endpoint url:

   ```python
   from django.views.decorators.csrf import csrf_exempt
   from graphene_django.views import GraphQLView

   urlpatterns = [
      # ...
      url(r'^graphql', csrf_exempt(GraphQLView.as_view())),
   ]
   ```

4. Install the frontend:

**Note**: Vuejs is supported out of the box but this can be adapted to any frontend

Grab the `Page.vue` component:

   ```bash
   wget https://raw.githubusercontent.com/synw/django-sfp/master/frontend/src/components/Page.vue
   ```

Install the dependencies:

   ```
   npm install --save vue-apollo // or vue add apollo if you use vue-cli
   npm install --save @fortawesome/fontawesome-svg-core
   npm install --save @fortawesome/free-solid-svg-icons
   npm install --save @fortawesome/vue-fontawesome
   ```

Font-Awesome is for the spinner loading icon (only this icon will be included in the build, 
not the whole lib). Vue-router must be installed
   
5. Add a frontend generic route:

   ```javascript
   import Page from './path/to/my/components/Page.vue'

   routes: [
      // ...
	  {
	     path: '*',
	     name: 'Page',
	     component: Page
	  },
   ],
   ```
To make links: ``<router-link :to="{ name: 'Page', params: { 0: '/myurl' }}"></router-link>``

Usage
-----

Create a ``pages`` folder in the Django project static directory. Any html file you include there will get served as
a static page.

For example::

* The url ``/about/`` will render ``static/pages/about.html``
* The url ``/about/team/`` will render ``static/pages/about/team.html``

Note: the first line of each file is the title of the page: ex:

   ```html
   My page title
   <div>My page content</div>
   ```

Edit pages online
-----------------

To edit pages at runtime you can use [django-dirtyedit](https://github.com/synw/django-dirtyedit)

