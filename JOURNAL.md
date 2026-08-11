---
title: "SnapVision"
author: "TheAbsoluteMin"
description: "Automated 3D scanner utilizing photogrammetry."
created_at: "2026-07-26"
---

# Log 1: July 26, 2026 - Initial CAD Attempt - 3 hours
Timelapse <a href="https://lapse.hackclub.com/timelapse/oqR18RJn2kxE">link</a>.

Oftentimes, when I am designing a case for a project through CAD, I need to reference the dimensions and physical models of real world objects. However, obtaining measurements and replicating intricate designs on some objects and electronics can be difficult and time-consuming. Thus, I decided to build a 3D scanner that uses photogrammetry to automate the generation of 3D files for me, which can greatly expedite the engineering and design processes.

I began working on the CAD model for the 3D scanner, and I wanted to create a polygon shaped base.

<img width="2542" height="1199" alt="image" src="https://github.com/user-attachments/assets/93bd8bf1-6679-47a5-ad94-9d9f4c29d862" />

However, I decided that the circular base was more elegant and simple to implement.

<img width="2538" height="1200" alt="image" src="https://github.com/user-attachments/assets/815c9418-31d3-4783-ab48-c95576c9aad7" />

It was especially difficult to orient the camera in a natural place, but with some time, I was able to work around the camera so it would fit in.

<img width="2554" height="1206" alt="image" src="https://github.com/user-attachments/assets/2271ae5d-c7f8-4086-abf4-a19e006b4c70" />


Tomorrow, I will continue to plan and construct the 3D scanner case!

**Total time spent: 3 hours**

---

# Log 2: July 27, 2026 - CAD Part 2 - 1 hour
Timelapse <a href="https://lapse.hackclub.com/timelapse/i1yO9gOfZwh6">link</a>.

With the basic design finished, I worked on the internal components of the 3D scanner case, including holes and channels for wiring and electronics, especially the camera that is isolated far from the Raspberry Pi 4.

<img width="2551" height="1191" alt="image" src="https://github.com/user-attachments/assets/235b9f7e-cf2b-4c89-80f0-41dc642ef630" />

Underneath the case, I made room for the battery, Raspberry Pi 4, and DC motor with vents to dissipate the heat when the project runs.

<img width="2538" height="1193" alt="image" src="https://github.com/user-attachments/assets/9cb66a42-3c2a-41cf-8309-a566aa3f8b17" />

This is what the model looks like as of now:

<img width="681" height="932" alt="image" src="https://github.com/user-attachments/assets/9fbfdd0e-8b4c-4950-9d39-6de6dc3aa596" />



I will attempt to 3D print the pieces next time to evaluate them physically.

**Total time spent: 1 hour**

---

# Log 3: July 28-29, 2026 - CAD Part 2 - 5.6 hours
Timelapse <a href="https://lapse.hackclub.com/timelapse/_uOzVr4UmdGI">link</a>.

After finding a Hosyond 5 inch DSI display, I felt motivated to adapt my design to offer a more sleek appearance.

<img width="801" height="852" alt="image" src="https://github.com/user-attachments/assets/84325cbc-89e5-4fb7-afb6-1ddf40156abb" />

Initially, I wanted to use only a single backdrop wall for the camera, but the design did not look appealing.

<img width="2545" height="1201" alt="image" src="https://github.com/user-attachments/assets/1c19b67e-1512-4d10-b015-d3cd73a9e832" />

However, with some research, I found great inspiration from the Formlabs 3D Printer.

<img width="813" height="882" alt="image" src="https://github.com/user-attachments/assets/ecc94b7b-b568-4302-aa3f-bfc5f9a7587c" />

And so, my work began. Since I had access to a laser cutter, I skipped the smooth fillets and bevels in order to use locking tabs, which would allow me to create the 3D scanner case much quicker. However, it was extremely time-consuming to create each tab! 

<img width="2538" height="1198" alt="image" src="https://github.com/user-attachments/assets/b794c1c9-131e-4925-aa13-2726c97c8b8a" />
<img width="2537" height="1195" alt="image" src="https://github.com/user-attachments/assets/69e479bf-b89d-4816-b7e4-9f3f128a1034" />

Integrating the DSI display was extremely hard, as the model CAD file for it took a lot of time for the system to process and handle, which greatly slowed down the workflow speed.

<img width="843" height="778" alt="image" src="https://github.com/user-attachments/assets/692bf57e-507c-4812-919d-353f8376c78b" />

In order to provide a dynamic and robust 3D scanner, I decided to implement another motor to control the camera distance from the rotating platter that would hold the object. This would enable the 3D scanner to adjust for large and small objects.

<img width="2547" height="1207" alt="image" src="https://github.com/user-attachments/assets/f384b7f3-8d71-400e-aa80-c8c0660bbd22" />

Right now, this is what my project looks like:

<img width="1097" height="1079" alt="image" src="https://github.com/user-attachments/assets/1713e1fe-b185-4dbd-b1fd-d42052bd815d" />

The colors shown are not the final colors of the project as I needed to see a clear contrast for each part, but I am hoping to make the top part a white frosted acrylic material that is somewhat clear while the bottom case will be a simple black color.

Today, SnapVision welcomed a new collaborator and friend, Ryan. During the final project week of the Tufts Engineering Design Lab Pre-College Summer Program, he agreed to work with me on fabricating my 3D scanner! While I worked extensively on the CAD design today, Ryan worked on the foundation of the code for SnapVision, and he tested out the camera, motors, and LEDs. Despite some slight difficulties with camera colors, he was able to get the code to take clear pictures and rotate the DC motor by a few degrees and repeat while running white LEDs.


I have begun laser cutting some of the sides and 3D printing some of the mechanical parts. I hope to finish assembling the project tomorrow!

**Total time spent: 5.6 hours**

---

# Log 4: July 29-30, 2026 - Coding and Assembly - 3 hours
Assembly Timelapse <a href="https://lapse.hackclub.com/timelapse/1YW8Dd9PgHda">link</a>.
Coding hours tracked on Hackatime.

After Ryan calibrated and tested the code that rotated and captured pictures with the camera and motor, I worked on writing the code to send those pictures to the Open Scan API.

Here is what Ryan's code looked like:

<img width="2120" height="1211" alt="image" src="https://github.com/user-attachments/assets/66d3e2ca-49dc-4f5d-8e96-162b02357470" />

He adjusted the code so that the firmware dynamically adjusted to users' choice of the number of pictures, which determined the angle step required to rotate the platter.

<img width="1049" height="618" alt="image" src="https://github.com/user-attachments/assets/8f43bf1b-df63-487a-9171-5c9bdd7b39bb" />

After calibrating the camera resolution and settings, he was able to allow the camera to capture quality pictures.

<img width="1630" height="1030" alt="image" src="https://github.com/user-attachments/assets/302f1cbf-361b-4bdf-b29b-246e32faa767" />

I had to learn how to use API code, and I quickly found it challenging.

I relied a lot on standard API code, and used a lot of place holder values as I did not have access to the Raspberry Pi 4 at that time.

<img width="968" height="382" alt="image" src="https://github.com/user-attachments/assets/feaf8269-c7b3-4934-b292-5e15f475f581" />

<img width="632" height="54" alt="image" src="https://github.com/user-attachments/assets/6654493b-980e-420c-bdcb-314c598263cf" />

<img width="2526" height="1407" alt="Screenshot 2026-07-30 013415" src="https://github.com/user-attachments/assets/0efc9ea8-ce6e-41dc-8adc-e0ff5a8fa295" />

When I finally was able to test and integrate the code with Ryan's, I found out quickly that it did not work... Then, I realized that I would have to read the Open Scan API GitHub and source code later!

After spending quite some time laser cutting and reprinting many parts due to inaccurate measurements and dimensions, my friend and I finally began on assembling the model! The box is mainly made up of laser-cut pieces, while pieces like the plane and walls that the camera views were 3D printed in gray to provide contrast when the API scans the pictures.

<img width="3000" height="4000" alt="20260729_163449" src="https://github.com/user-attachments/assets/0319233d-a65a-41ab-9596-2e115999b932" />

I had originally planned a sliding mechanism with a distance sensor that would move the camera with respect to the object on the platter, but after the coding tests, Ryan and I agreed that it was not necessary.

Also, I wanted the top clear case to be made out of frosted acrylic, but I later realized that Tufts program did not have any, so I used clear acrylic instead. 

<img width="4000" height="3000" alt="20260730_135755" src="https://github.com/user-attachments/assets/169769e7-8530-4672-bd44-f4126268e8fc" />

The bottom base box has two layers for structural stability, with black matte acrylic material supported by birch wood. An interesting obstacle I faced when printing these layers included the high amount of time the laser cutter required to print tiny grills!

<img width="4000" height="3000" alt="20260730_130937" src="https://github.com/user-attachments/assets/8efab011-1e39-4e64-88a1-4e5df8d839fc" />
<img width="3000" height="4000" alt="20260730_135745" src="https://github.com/user-attachments/assets/84bcfbde-aa48-447d-b10c-70a9f5a11982" />
<img width="1180" height="664" alt="image" src="https://github.com/user-attachments/assets/b0f28087-5196-4a2f-9eb8-e7a5cffcaeb8" />

With a lot of hot glue, Ryan and I were able to put together a nice case with a sleek touchscreen display!

<img width="4000" height="3000" alt="20260730_135735" src="https://github.com/user-attachments/assets/fe0401b6-d52d-4fad-8b8d-6661b289787c" />
<img width="3000" height="4000" alt="20260730_172717" src="https://github.com/user-attachments/assets/df00a238-f648-4634-aba8-14078497642d" />
<img width="3000" height="4000" alt="20260730_183625" src="https://github.com/user-attachments/assets/9b4831cc-2c98-4a73-86ef-7e96d9e174bd" />
<img width="3000" height="4000" alt="20260730_183635" src="https://github.com/user-attachments/assets/e05d18f4-eb5c-4c88-a2cf-93b5f4c3a4ba" />


I hope to soon write a polished and fully complete firmware for my project as the Tufts program is ending on July 31, 2026, so Ryan will no longer be able to help me with the project and coding. However, I hope I can finished it!

**Total time spent: 3 hours**

---

# Log 5: August 4, 2026 - Raspberry Pi 4 Setup and Firmware - 6 hours
Timelapse <a href="https://lapse.hackclub.com/timelapse/Z6yoEgbLf6Xv">link</a>.

Wow, do I have a story to tell you! I was experimenting with the DSI display screen, and I wondered if I could display CAD files! Thus, I tried to run the lightweight F3D, a 3D viewer application, to display a simple .obj file.

<img width="875" height="449" alt="image" src="https://github.com/user-attachments/assets/a05462f7-84c9-4a68-9406-5fae8c3d7b07" />

However, I got the following error:

<img width="987" height="150" alt="image" src="https://github.com/user-attachments/assets/f8bdee08-88d3-489d-90e4-f28f6c283a9d" />

Apparently, my display screen did not have access, so I searched up a solution and found this code command:
> subprocess.run(["xhost", "+local:"])

However, it did not work still, so with further research, I came to the conclusion that it needed the Raspberry Pi 4 to run on X11 rather than the wayland session, so I tried to change that with some Pi terminal commands.

Long story short, it was not successful!

I tried to adjust the settings in the configuration tool, but the F3D viewer still did not run.

<img width="997" height="221" alt="image" src="https://github.com/user-attachments/assets/33c55219-71ad-4eed-ab20-e1e91dd86b8e" />

I tried to edit lightdm's session settings to default to X11, but that only gave me more errors! After rebooting the Pi 4, my display screen showed a really worrying page.

<img width="1087" height="534" alt="image" src="https://github.com/user-attachments/assets/9ae05675-d9fc-4341-9537-bd68e7b8cd10" />

I was locked out of my virtual desktop! However, I was fortunate that the Jupyter Labs web server that the Tufts University program had installed still worked, so I opened a the Pi terminal from there! After reopening the lightdm settings, I realized that the Pi 4 had other settings that locked it in the Wayland session that I had missed and not changed. Thus, as the Pi 4 was in a conflicting state, I attempted to undo my work, but each terminal command and file edit seemed to make it worse, until I was not sure what I had done... I tried to reinstall the old packages for Wayland that I had accidentally deleted, and it did not work.

<img width="1227" height="1293" alt="image" src="https://github.com/user-attachments/assets/61cbdcf6-df58-4dc5-a602-e1680629fae7" />

Files seemed missing and corrupted, and each command I typed may have actually made my situation worse rather than fix the problem. 
<img width="1124" height="567" alt="image" src="https://github.com/user-attachments/assets/e19c96c5-8077-4813-9eb8-395de9e86031" />
<img width="1018" height="551" alt="image" src="https://github.com/user-attachments/assets/e064c25e-86bf-46c9-b67e-83a297568243" />

Thus, I finally decided to start anew and flash a brand new Pi OS. It was a difficult decision as that would mean the software and tutorials implemented by the Tufts University program would be erased, but I really wanted a working display screen! Flashing the new Pi OS was challenging as I did not have an SD card reader. With some reading, I found a way to flash the software onto a USB drive, which could be plugged into the Pi to start it. Then, I could use Raspberry Pi Imager to flash the cleaned micro SD card with the clean software! 

It took a few tries to flash the large software onto the USB drive since initially, the balenaEtcher software threw errors at the end after taking a long time to execute the flash!

<img width="2559" height="1445" alt="image" src="https://github.com/user-attachments/assets/5e5241d9-4cea-426e-afd9-0fa237d341d8" />

Then, I switched to the Rufus software, and it finally worked!

<img width="876" height="1026" alt="image" src="https://github.com/user-attachments/assets/a1557c41-04d4-4e79-a98d-1a7241a7e48d" />

The Pi 4 read the USB drive, and I was able to set up my preferences and flash the micro SD card with the clean Pi OS!

After all that painful work, I installed the GoPiGo3 and Jupyter Lab softwares again, so I could keep the same quick workflow where I could instantly test and run code. I ran into some errors with the GoPiGo3 software as it seemed to have needed other libraries like swig to help install and compile it.

<img width="1446" height="678" alt="image" src="https://github.com/user-attachments/assets/11968992-e7fa-4ccd-9388-0c31ecccd153" />
<img width="1880" height="1002" alt="image" src="https://github.com/user-attachments/assets/ff6572b8-a33c-4f53-a359-eb55e01197b2" />

After setting up the Jupyter Lab web server, I could finally begin coding. Of course, the code no longer natively worked in this new environment since I no longer had my program's software and libraries! Thus, I had to update the code so that it would work with standard libraries. The camera was especially difficult to reconfigure correctly so that it still took sharp images!

<img width="1113" height="442" alt="image" src="https://github.com/user-attachments/assets/e36530b8-721a-407c-a190-e209afd3d0c1" />


I began to adapt the Open Scan API's example code, and I hope to continue to integrate the API automation code into my project next time!

**Total time spent: 6 hours**

---

# Log 6: August 6-7, 2026 - More Coding - 3 hours
Timelapse <a href="https://lapse.hackclub.com/timelapse/wpJM3WVz891h">link</a>.

With the guidance of the example firmware in the Open Scan API GitHub, I integrated the firmware that would connect with the API server.

<img width="1273" height="762" alt="image" src="https://github.com/user-attachments/assets/949f601b-9b41-40c5-af74-a461124fac1a" />

The API required a lot of verification steps, including token and photo data checks, before I could actually send the images over in the form of ZIP files.

<img width="1523" height="531" alt="image" src="https://github.com/user-attachments/assets/3106839f-b1e9-42eb-86e5-7df7b42f8688" />

I realized that the example firmware defaulted to returning an email with a ZIP Dropbox download! Since I wanted to make my 3D scanner automated, I needed to get the 3D model directly without manually opening up an email.

First, I tried to access my email through IMAP in order to retrieve the latest email.

<img width="1009" height="673" alt="image" src="https://github.com/user-attachments/assets/9c4cbaae-fc49-4d04-8c67-e9d7da950676" />

Then, I could find the Dropbox download link in that email.

<img width="1302" height="470" alt="image" src="https://github.com/user-attachments/assets/ea7de8bd-5275-4d4e-b13c-573d0a71137a" />

However, considering the safety and security implications of using an email credentials for this application, I wondered if there was a better way. Fortunately, after reading again through the API's GitHub README, I found an interesting word in the response fields of the Get Project Info endpoint.

<img width="1072" height="1050" alt="image" src="https://github.com/user-attachments/assets/3d4b66cb-b5e0-4768-95d1-2530ae46df17" />

With this, I tested to see if I could simply retrieve "dlink" in the firmware after the 3D model was created.

<img width="1037" height="582" alt="image" src="https://github.com/user-attachments/assets/66791d3b-595b-4d12-9a30-ec5f5ba83f9f" />

After downloading the Dropbox ZIP file with the firmware, I could extract it to access the .obj 3D model file! As a bonus, I decided to use F3D viewer to display the 3D model at the end!

<img width="1658" height="303" alt="image" src="https://github.com/user-attachments/assets/51bbfe6b-5c35-46bc-81b0-94b9f8cbc193" />


Next time, I will test out the code again to make sure it works, so I can begin finishing up the GitHub repository!

**Total time spent: 3 hours**

---

# Log 7: August 9, 2026 - GitHub Work and Code Testing - 3 hours

Today, I extensively worked on putting together the GitHub repository files. Getting all the pictures and files together took quite some time, as I had to disassemble my project and then put it back together step by step in order to include assembly instructions!

<img width="1810" height="1259" alt="image" src="https://github.com/user-attachments/assets/d24500a1-90c1-4e07-8399-41e5d97cec1d" />
<img width="2013" height="1279" alt="image" src="https://github.com/user-attachments/assets/0943e5f0-d1ef-438e-8f5a-373300ef4d1a" />

Then, I spent an incredibly long amount of time just trying to get one full successful run of the firmware. However, the Open Scan API did not seem to work. There were data transmission errors despite no change of the working code from yesterday!

<img width="1942" height="554" alt="image" src="https://github.com/user-attachments/assets/7bf71871-d9cf-4d36-9abe-d8e596e84b1c" />

My first attempt in fixing this problem included reverting the file naming to the original one set by Open Scan. However, that did not work.

After comparing my API code with the example code from Open Scan API, I figured that there must have been a problem with the images that were being put into a ZIP file. Apparently, the Open Scan API code explicitly checked for allowed photo types like .jpg in order to prevent hidden files in the camera folder to be included in the ZIP file that would be sent over to the API server. I implemented that and the data transmission errors went away! 

<img width="836" height="176" alt="image" src="https://github.com/user-attachments/assets/a244ee14-3d9c-4e16-bc17-d90c173686b9" />

However, a key problem with the API is that it does not always return dlink in its project information endpoint. Thus, I may have to revisit the email IMAP code.


I hope I can finally obtain a working video of SnapVision working!

**Total time spent: 3 hours**

---

# Log 8: August 10, 2026 - Firmware Fixes - 1.1 hours
Timelapse <a href="https://lapse.hackclub.com/timelapse/publish/ZiJJ-kKts3R0">link</a>.

Today was a big day! After a long, hard fought war against my firmware, I finally was able to achieve a complete and successful run of the firmware! However, there were some notable problems with the code that I had to solve.

First, my previous code logic form downloading the ZIP file from the API returned an "is a directory error".

<img width="827" height="296" alt="image" src="https://github.com/user-attachments/assets/9caef2b4-3666-49e7-848a-8703fa16f8d1" />

Thus, I had to use "os.path.basename(dlink)" in order to extract the end of the URL path, so that the firmware could download to a working folder path.

<img width="1132" height="216" alt="image" src="https://github.com/user-attachments/assets/2ef21ad9-7d71-471f-8aa0-878df56af45c" />

After some testing, I confirmed Open Scan API's interesting quirk where it would sometimes not include a downloadable link in its dlink API endpoint. To handle this, I implemented an adaptive handling feature where the code would first check the dlink endpoint before using an alternative method to get the ZIP download link. This is where the IMAP code, which I had initially rejected, now shines.

Now, instead of blindly targeting the latest email, the firmware targets the latest email from Open Scan API and finds the dlink in the email text, so I can download the ZIP file later.

<img width="1299" height="957" alt="image" src="https://github.com/user-attachments/assets/828a2fda-c705-4bb8-8f0f-d982b58785b5" />

A run of the firmware proved that my code finally worked, even when Open Scan API did not include the download link!

<img width="1677" height="313" alt="image" src="https://github.com/user-attachments/assets/8ba5e200-8139-40ab-9ad6-eaf3f10833ac" />

With some final edits to my GitHub repository, I hope I can finish SnapVision soon!

**Total time spent: 1.1 hour**

---
