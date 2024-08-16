# 0x00. Pagination
### Description
This project is about implementing pagination in a web application.

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/12/3646eb02de6527ca5d83.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240816%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240816T165549Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=16b222c372a2b079d3c98a60666bdae6d0edf1bc1a100b95efdbc25871d53baf) ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/12/746187b76bea1f46030e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240816%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240816T165549Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ed21a048a478fe6e4d186898ef8d4ebc7179ca1233e99cdde32b9e4b86ee34c3) ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/12/665ce871c2ecc66a8e71.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240816%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240816T165549Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0be8cbcb24b0d341aedaf30bd53d2ace8e7d8e2764cb8f04c22530d0c20144c4)

## Resources

**Read or watch:**

- [REST API Design: Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination "REST API Design: Pagination")
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS "HATEOAS")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/ "explain to anyone"), **without the help of Google**:

- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Requirements

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5.*)
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

## Setup: `Popular_Baby_Names.csv`

[use this data file](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240816%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240816T171327Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=97640ad00f1e038a11586af0884163c459a90446cfe20c0c4900b9dad5465892 "use this data file") for your project


## Tasks