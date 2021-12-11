<h3>First run: </h3>

[Copy headers ](https://user-images.githubusercontent.com/43696206/145660715-472e4c65-86de-453f-86fc-5bb14028f448.png)(with cookies) of POST license request from browser to headers.py like dictionary.</br>

```
pip install -r requirements.txt # if doesn't work try pip3
py l3.py
Input MPD URL: https://site.ru/.../.../filename.mpd
License URL: https://cms.35mm.online/umbraco/api/products/473/drm/widevine?platform=BROWSER&type=MOVIE
```

Works only if the site does not require specific json-formatted data in the license request. 
And if it requires and you want to add its support, write to issues specifying the required json-formatted fields and the algorithm for their formation (if not static).
</br> Examples:</br>
1.  Normal work: </br>
   ![Normal work](https://user-images.githubusercontent.com/43696206/145641480-bf3a07a6-2d6e-4dee-9398-b4ecdf8bf273.png) </br>
2. Server did not issue a license, as it requires additional json-formatted data: 
  ![error_teapot](https://user-images.githubusercontent.com/43696206/145643061-8e44b226-a3c2-4c44-8c62-6db84e582d9e.png)</br>
3. If "Unable to find PSSH in mpd" - write about this error to issues attaching a link to mpd.</br>

Further about kinopoisk (hello to compatriots):</br>
Not working yet.
It is necessary to find out how the POST request is signed (the signature field in the request payload). 
It looks like a simple hash of sha1, but from the looks of it, this is not it, but the Amazon's AWS Signature Version 4. Or I am doing something wrong and everything is much easier...
Any ideas are appreciated, write to issues.

[Parsed payload of license request](https://user-images.githubusercontent.com/43696206/145263764-349dd8be-58ec-4d42-9524-4a098b0fe5e3.png)

