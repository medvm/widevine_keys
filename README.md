<h2>Important info</h2>
From December 14, 2021, CDM android_generic_4464 is gradually ceasing to work on most major VODs. Accordingly, since the script is based on this CDM, from this day on without replacing the CDM with the "non-leaked" one it will not work. How to fix this can be found in Google (if you need help with this - write to https://t.me/medvm).

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
3. If "Unable to find PSSH in mpd" - use [this tool](https://tools.axinom.com/generators/PsshBox) to get it manually or write to issues attaching a link to mpd</br>