1.1 OVERVIEW
Our objective in the Guided Project is to forecast the outcome of the numerous
professional overseas applicants who submit H-1B visa applications each year. In
this instance, we employed it to frame the issue as a classification problem and to
produce a forecast case status for the application. The applicant's characteristics
serve as the input for our system. In the United States, a non-immigrant visa called
an H-1B enables foreign people to work in professions that call for specialised
knowledge and a bachelor's degree or higher in the relevant field.
1.2 PURPOSE
Before submitting an application to the USCIS for this visa, the applicant must
already have an employment offer from a company in the US. We think that this
prediction algorithm could be a helpful tool for prospective H-1B visa candidates
as well as potential employers.
We will feed the model with the dataset including the necessary fields by which the
machine may classify the case status as certified or refused in order to predict the
case status of the applicants.
The uncertainty and lack of openness in the selection process are two current
issues with the H1B visa prediction procedure. There is a yearly cap on the
amount of H1B visas given due to the program's high demand. However, the
random lottery mechanism used to choose H1B visa beneficiaries can be
annoying for both companies and potential employees.
The existing approach does not consider elements like the requirements,
abilities, or demand for particular employment roles. As a result, highly
qualified persons who would considerably boost the American economy might
not be given visas, while people with less impressive credentials might get them
by accident.
Employers who need to plan their staff and find the best employees face hurdles
as a result of this uncertainty. Additionally, it causes aggravation for those who
put forth time, energy, and money into the visa application procedure just to
have a random drawing determine their prospects.
2.2 PROPOSED SOLUTION
We developed this Visa Approval status prediction by using the Python language
which is a interpreted and high level programming language and using the
Machine Learning algorithms. for coding we used the Jupyter Notebook
environment of the Anaconda distributions and the Spyder, it is an integrated
scientific programming in the python language. For creating an user interface for
the prediction we used the Flask. It is a micro web framework written in Python. It
is classified as a micro frame work because it does not require particular tools or
libraries. It has no database abstraction layer, form validation, or any other
components where pre-existing third-party libraries provide common functions,
and a scripting language to create a webpage is HTML by creating the templates to
use in th functions of the Flask and HTML.
3.2 SOFTWARE REQUIRED
1. Jupyter Notebook Environment
2. Spyder Ide
3. Machine Learning Algorithms
4. Python (pandas, numpy, matplotlib, seaborn, sklearn)
5. HTML
6. Flask
7. 4.EXPERIMENTAL INVESTIGATIONS
The dataset we used for this study was taken from H-1B_Kaggle.More than 10L
H-1B Visa user records are contained there.It had one label and seven traits that
could be analysed as attributes. The screenshot of the data set we utilised below
illustrates these characteristics. CONTEXT STATUS: We did not include the
cases 'CERTIFIED-WITHDRAWN' and 'WITHDRAWN' since
'WITHDRAWN' decisions are either made by the petitioning employer or the
applicant, therefore they are not indicative of USCIS's future actions.
'CERTIFIED' cases received a label of 1 while 'DENIED' cases received a label
of 0. Positions are listed with the notation "Full Time Position = Y; Part Time
Position = N". They were formatted as "Full Time Position = 1; Part Time
Position = 0". YEAR: The year that the application was submitted. The data
was transformed into a one-hot-k format. PREVAILING WAGE: Prevailing
wage is the typical salary given to workers with comparable credentials in the
desired field of employment. The remainder of the data was used without the
outlier terms. APPLICATIONS PER EMPLOYER_NAME: We built a feature
to count the number of H-1B applications submitted by each employer. We
eliminated data points from petitions submitted by employers with fewer than
four applications. This processing phase unavoidably discards applications
submitted by small businesses, however it greatly aids in correcting misspelt
company names. For the success rate by employer, a functionality was
developed. Apps by Social Name: The federal occupational classification
system known as SOC stands for Standard Occupational Classification System.
We removed data points with SOC kinds that appear less than four times in the
data and built a feature for the quantity of H-1B applications by SOC type.
Undesirably, this processing stage eliminates applications for jobs that are
unusual, although it aids in cleanup. WORKSITE: The format for the data is
"City, State". We reduced the data to a one-hot-k representation and only
included "State". Following the aforementioned pre-processing processes, we
divided the training, A total of 1.2 million examples made up the training set.
We established two versions and test sets in order to make sense of the error
analysis later on because our dataset has a built-in bias towards the
"CERTIFIED" label. The initial development and test collections, which each
had 400K samples, were also unbalanced. More specifically, to mimic the
original dataset, almost 90% of the samples had a "CERTIFIED" label. By
manually picking an equal number of "CERTIFIED" labelled examples as
"DENIED" labelled cases, the second version of the development and test sets
were balanced.
9. CONCLUSION
The selection for H visas has increased every year over the past ten years, so
the goal of this challenge is to develop a tool that will inspire every person
going through the H1B visa application process and accurately forecast
whether or not their application will be accepted. Additional details about
the Standard Occupational
Classification (SOC) can be combined and put into practise in accordance
with the H-1B Visa preference procedure. The income feature on this data
set can be accurately mounted to a range of incomes using the income
opinions and levels under SOC. From there, it is possible to classify visa
applications according to career positions and geographic preference.
Additionally, beautiful beauty algorithms that are not discriminative models
can be tested with this method, and their results can also be evaluated. In
comparison to all of the fantastic algorithms that can be gifted to carry out
the evaluation activities, the Random Forest classifier works right right right
here with the superior accuracy. Here, the Random Forest Algorithm was
used to enhance and enrich the data, and as a result, we were given an
accuracy of 83.06 percent. As a result, this set of recommendations is the
best available for the prediction of H1B visa approval. It has become
necessary to build a tool to accurately track down H1B visa approval due to
the rising trend of H1B visa applicants. Therefore, we are able to seek for
the H1B visa approval rate using the useful assistance of a number of device
learning sophistication algorithms. For international workers coming to the
US, this can be highly advantageous.
