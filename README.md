# django-multitenant-app-basic-framework
This is a python django basic framework for developing a multitenant application where each major client can have a subdomain in your application with a dedicated schema and a shared database for all clients.

multi-tenant applications allow you to serve multiple customers with one install of the application. Each customer has their data completely isolated in such an architecture. Each customer is called a tenant.

Tenants may be given the ability to customize some parts of the application, such as the color of the user interface (UI) or business rules, but they cannot customize the application's code.

I made it possible to create a tenant manually. Inorder to create a tenant/client in the project you'll have to type in the command 'python client.py <tenant_name>' you can override this and create your own method of creating a tenant using the browser. It is also possible to et the details of a tenant using command 'python client.py get_tenant <tenant-name>'

To visit the specified client on the browser using the subdomain name on localhost. You must edit the windows hosts file and add in the subdomain address.

Feel free to clont this repo and happy coding to you.
