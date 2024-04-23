> [Back](../Reviews/reviews.md)
<div style="text-align: right"> Myat Ma De May Phuu Ngon</div>
<div style="text-align: right"> 26002304901</div>
<div style="text-align: right"> April 19th 2024</div>

## Design Patterns for User Interface for Mobile Applications

<div style="text-align: justify"> This paper is a collection of user interface (UI) design patterns for mobile applications which could help in designing the UI for our application. It outlines the structure of the collection, grouping patterns into three main problem areas with two specific problems from each area.This is helpful for identifying patterns and a thorough overview of UI design issues for mobile apps. The three main problem areas are utilizing screen space, interaction mechanisms, and design at large. 
Regarding utilizing screen space, horizontal scrolling is said to be one problem as part of screen space in general. Horizontal scrolling is worse than vertical scrolling as the users lose more context when scrolling horizontally. Here, changing the layout which is to increase more vertical scrolling is one solution to this problem. However, I doubt we will be having any horizontal scrolling for selecting elements in our app. Another problem in the same field is handling crowded dialogs when the software keyboard is shown and hidden. This results in less room for normal interaction and how to resize is a consequence. To avoid this, dynamic resizing by either deciding a resizing rule for each window and applying that as tailored code for each window or having a general layout adjustment algorithm doing it for all windows can be used. This point is lightly noted as we need user input for a shrine name in our app and when we have an issue with keyboard display, we can use this method.<div>
<br>
<div style="text-align: justify"> Regarding interaction mechanisms, mechanisms for entering text is a problem especially for personal digital assistants with very small keyboards and the solution is to have an auto-complete suggestion text. However, this is not an issue in our app. One important thing to note is that we should include a spinner or buttons for time display in choosing a specific period in our app and check boxes for filtering categories. Another problem in the same field is interacting with applications without using a stylus which again is not really related to our app. One good thing to note here with its respective solution is that we should not make tab buttons too small and more finger-friendly buttons.<div>
<br>
<div style="text-align: justify"> Regarding design at large, one main problem is the design that supports branding, is aesthetic, and utilizes screen space optimally. If the branding includes a graphical profile, the UI controls will look different from platform standard. This may cause usability issues, being added for aesthetic reasons may decrease the affordance of the control and take up space. One solution is to include the company logo in various places of the UI and use colors and other visual elements from the graphical profile of the company in UI controls and backgrounds. For our app, this point is essential as we also need branding. The last problem in the same field is user interaction during waiting for long-lasting operations to complete and will probably make mobile users impatient. Few solutions that could be useful to our app are providing a wait cursor with a message saying “please wait…”, or to inform the user that something is happening, and indicate progress with a counter and/or a slider/gauge that shows the percentage of time spent.
By taking notes of the UI design problems and solutions in this paper, we will be able to make an app that is efficiently working and aesthetic with our own brand which will later be appealing to our users.<div>

<h2>Reference</h2>

Design patterns for user interface for mobile applications
Nilsson, E. G. (2009). Design patterns for user interface for mobile applications. Advances in engineering software, 40(12), 1318-1328.
