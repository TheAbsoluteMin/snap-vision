---
title: "SnapVision"
author: "TheAbsoluteMin"
description: "3D scanner utilizing photogrammetry."
created_at: "2026-07-26"
---

# SnapVision Development Log

## Log 1: July 26, 2026 - Initial CAD Attempt - 3 hours
Timelapse <a href="https://lapse.hackclub.com/timelapse/oqR18RJn2kxE">link</a>.

### Inspiration:
Oftentimes, when I am designing a case for a project through CAD, I need to reference the dimensions and physical models of real world objects. However, obtaining measurements and replicating intricate designs on some objects and electronics can be difficult and time-consuming. Thus, I decided to build a 3D scanner that uses photogrammetry to automate the generation of 3D files for me, which can greatly expedite the engineering and design processes.

I began working on the CAD model for the 3D scanner, and I wanted to create a polygon shaped base.

<img width="2542" height="1199" alt="image" src="https://github.com/user-attachments/assets/93bd8bf1-6679-47a5-ad94-9d9f4c29d862" />

However, I decided that the circular base was more elegant and simple to implement.

<img width="2538" height="1200" alt="image" src="https://github.com/user-attachments/assets/815c9418-31d3-4783-ab48-c95576c9aad7" />

It was especially difficult to orient the camera in a natural place, but with some time, I was able to work around the camera so it would fit in.

<img width="2554" height="1206" alt="image" src="https://github.com/user-attachments/assets/2271ae5d-c7f8-4086-abf4-a19e006b4c70" />

### Future work:
Tomorrow, I will continue to plan and construct the 3D scanner case!

---

## Log 2: July 27, 2026 - CAD Part 2 - 1 hour
Timelapse <a href="https://lapse.hackclub.com/timelapse/i1yO9gOfZwh6">link</a>.

With the basic design finished, I worked on the internal components of the 3D scanner case, including holes and channels for wiring and electronics, especially the camera that is isolated far from the Raspberry Pi 4.

<img width="2551" height="1191" alt="image" src="https://github.com/user-attachments/assets/235b9f7e-cf2b-4c89-80f0-41dc642ef630" />

Underneath the case, I made room for the battery, Raspberry Pi 4, and DC motor with vents to dissipate the heat when the project runs.

<img width="2538" height="1193" alt="image" src="https://github.com/user-attachments/assets/9cb66a42-3c2a-41cf-8309-a566aa3f8b17" />

This is what the model looks like as of now:

<img width="681" height="932" alt="image" src="https://github.com/user-attachments/assets/9fbfdd0e-8b4c-4950-9d39-6de6dc3aa596" />


### Future work:
I will attempt to 3D print the pieces next time to evaluate them physically.

---

## Log 3: July 28-29, 2026 - CAD Part 2 - 5.6 hours
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

### Future work:
I have begun laser cutting some of the sides and 3D printing some of the mechanical parts. I hope to finish assembling the project tomorrow!

---

## Log 4: July 29-30, 2026 - Coding and Assembly - 3 hours
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

When I finally was able to test and integrate the code with Ryan's, I found out quickly that it did not work... Then, I realized that I would have to read the Open Scan API Github and source code later!

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

### Future work:
I hope to soon write a polished and fully complete firmware for my project as the Tufts program is ending on July 31, 2026, so Ryan will no longer be able to help me with the project and coding. However, I hope I can finished it!

---
