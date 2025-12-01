[//]: # "# Potential Changes:"

[//]: # "- add confidence scores"
[//]: # "- change sub categories: Context, Background Knowledge, Reasoning"
[//]: # "- make comment field more general"
[//]: # "- move ungrammaticality statement more to the beginning"
[//]: # "- reword task description to avoid negation?"

# Annotation Guidelines: Implicit Meaning

The goal of this annotation task is to find sentence pairs where one sentence contains **implicit meaning** that is made explicit in the other. More specifically, this means that, even though not everything is stated explicitly in the first sentence, **the understanding of the text would not change for most readers** when the information is added.

The data that will be presented to you is from a dataset based on wikiHow articles. For every item you will first be shown the name of the article from which the texts were taken. Below that you will find two almost identical texts where one sentence is highlighted in bold. The bold sentence in the second text contains an additional element, marked in :blue-background[blue]. Do not worry about other changes in the sentence. 

Below the texts you will find two buttons (:grey-background[Yes] and :grey-background[No]) as well as a comment section. If you check the :grey-background[No] button, four more checkboxes will appear. You will further find five more checkboxes where you have to select how confident you are in your selection before you can proceed. You can check out this mini example here and play around with it:

---
:grey-background[*Article name:*] &emsp;How_To_Annotate_This_Task.txt

Read the following text and focus on the **bold sentence**. 
 

> This is how the annotation task will look like.  
> **Check the box below.**  
> Don't forget to select your confidence score before you proceed!  
 
\
:grey-background[Now read the modified text:] 
 

> This is how the annotation task will look like.  
> **Check the box below :blue-background[by clicking on it].**  
> Don't forget to select your confidence score before you proceed!


[//]: # ":grey-background[Does changing the bold sentence affect your understanding of the text?]"
\
:grey-background[What would most readers say?]

:grey-background[Would altering the bold sentence meaningfully change how they understand the text?]

==SPLIT==

---

During the annotation task, select :grey-background[No] if you think that changing the bold sentence in the given context would not affect the understanding of the text for most readers, even though the first text does not state all information explicitly. If you do this, please specify the reason for your decision by ticking the relevant checkboxes among the ones that will appear. You can choose from the following categories:

---

### Indicators for Implicit Meaning

#### **1. Context**
The added information is recoverable from the context (including the article title). In the following example, the reference “doll” can be inferred from the title of the article.

**Example:**  
*How_To_Care_for_an_Uglydoll.txt*  
* When you buy it, it has a tag with its name and its personality.  
  **Look at the tag.**  
  Now you know what it likes so far.

* When you buy it, it has a tag with its name and its personality.  
  **Look at the tag :blue-background[of the doll].**  
  Now you know what it likes so far.

---

#### **2. Logical Reasoning**
The added information is a logical premise or consequence of the given text. In the following example, the fact that you do not have to buy something if you already possess it can be logically inferred by most readers.

**Example:**  
*How_To_Shorten_a_Bike_Chain.txt*  
* **Purchase a universal chain tool.**  
  This tool pushes the pins out of your chain to allow link removal.

* **Purchase a universal chain tool :blue-background[if you don’t have one].**  
  This tool pushes the pins out of your chain to allow link removal.

---

#### **3. Background Knowledge**

The information in the added text was already anticipated due to existing background knowledge. For instance, most readers would know that teachers usually prepare assignments for their students. This category might sometimes correlate with *Context*.

**Example:**  
*Do_an_Assignment_on_Google_Classroom.txt*  
* As a student, you can submit an assignment on Google Classroom by logging into your student profile on Google Chrome and accessing your class list on the Classroom site. 
  **Teachers can create and distribute assignments by logging into Chrome as well […].**

* As a student, you can submit an assignment on Google Classroom by logging into your student profile on Google Chrome and accessing your class list on the Classroom site.
  **Teachers can create and distribute assignments :blue-background[to their students] by logging into Chrome as well**

---

**Note:**  
A sentence pair may match multiple categories.  

[comment]: # (For example, the third example could also fall under **Context**, since what one might be surprised about is evident from the immediate context.)

If you think the added information is implicit meaning but **none of the criteria above** apply, please tick the **Other** checkbox and explain your reasoning in the comment section next to it.

---

### Indicators for New Information

If any of the following apply, select :grey-background[Yes]. These suggest **new information** rather than implicit content:

#### **1. Addition changes the core meaning**
The addition fundamentally changes the meaning of the original sentence.

**Example:**  
*How_To_Calculate_Z_Scores.txt* 
* **Find the sample mean.**  
  Add together the values of all of the samples.

* **:blue-background[Subtract each sample from] the sample mean.**  
  Add together the values of all of the samples.

---

#### **2. Added information is too specific**
The added information introduces specific entities, concepts or events that most readers cannot be expected to know about.

**Example:**  
*How_To_Put_Game_Saves_on_Your_PSP.txt*  
* Put the game in that you got the save data from and see if it works.  
  **Don't forget to remove the cable.**

* Put the game in that you got the save data from and see if it works.  
  **Don't forget to remove the cable :blue-background[by Apple].**

---

Feel free to share any observations or thoughts in the comment field! This might help us understand your decision even better.

Finally, please indicate your level of confidence at the bottom of the page. 1 means :grey-background[Not confident at all] and 5 corresponds to :grey-background[Absolutely sure].

> Please note that, since the data is taken from a wikiHow dataset, the text might sound ungrammatical or unnatural at times. Do not let this distract you from the task. When you feel like you cannot complete the task due to the ungrammaticality of the text, select :grey-background[Yes] and write a note in the comment section. 
