# Curriculum Vitae

<img src="../me.JPG" alt="me" width="200"/>

## About Me

Hi! My name is Felipe Marques da Silva, I'm 29 years old, and I live with my girlfriend and our two cats in São
Paulo/SP. Although I graduated as an Electrical Engineer, I've been working as a Software Developer and in related
fields since I graduated. Most of my knowledge in Software Engineering was acquired through self-teaching, and I've also
learned a lot from each of the professional experiences I've had. I can listen to, write and read English at an advanced
level, and I speak it at an intermediate level.

I have experience in designing resilient and scalable software architectures, and in producing simple, testable, and
maintainable code in Python. I have solid skills in technical leadership, object-oriented programming, SOLID principles,
software versioning with Git, Clean Code, AWS cloud services, unit and integration testing, and HTTP APIs.

### Contact Information

**Phone:** +55 16 99172-2315

**Email:** femarques01@gmail.com

## Education

#### Software Architecture Training (2021)

Software Architect Training Program promoted by Experian, with classes taught by Elemar Jr.

#### University of São Paulo (2018)

Bachelor of Electrical Engineering with emphasis on Electronics, São Carlos School of Engineering.

## Professional Experience

### **Senior Software Engineer** - *Itaú Unibanco* (05/2022 - Present)

I was the technical lead on a project to modernize the daily financial result calculation for part of the Treasury's
operations, for monitoring and operator verification.

> Previously, this process was done through a set of Excel spreadsheets and its main problems were the lack of
> robustness, slowness to execute the process (+5h/day), dependence on people to execute it, and technological resource
> limitations to handle the large volume of data.
>
> The process was divided into +50 routines, which could be dynamically triggered by HTTP endpoints exposed in a
> SwaggerUI. We designed a monolithic API, focused on use cases and divided into layers, achieving 85% unit test
> coverage,
> with very low maintenance and user support on a day-to-day basis.
>
> By the end of the project, the daily routines were executed automatically in less than 1 hour (-80%) with enormous
> confidence and robustness due to extensive test coverage. The reports were consumed by Excel, providing high user
> adoption and eliminating the need for a front-end.

**Technologies:** *Python3, Pytest, Pandas, FastAPI, SQLServer, SOAP, HTTP, Docker, Kubernetes, AWS*

During my time at the company, I was recognized for high performance, and also received a salary increase.

### **Backend Developer** (Mid and Senior) - *Experian* (01/2021 - 05/2022)

I was technical lead on a project to change the display of debt renegotiation offers from Serasa Limpa Nome, adding
a banner "Dropped R$ X" if the offer met certain business rules.

> The main complexities of the project were: the high volume of requests (10k-40k reqs/min); and adding the banner
> should not burden the offer page loading.
>
> We created a CQRS architecture (2 services) to generate and query the banners separately, and enabled A/B testing
> configuration and real-time roll-out of the functionality. We applied load tests to scale the services and created a
> dashboard to monitor the execution time of banner generation and query. Each step of the process emitted events for
> further statistical analysis.
>
> As a result, the apparatus was able to meet all functional and non-functional requirements using few computational
> resources, ensuring a smooth user experience. The entire project took approximately 5 months to be put into production
> and was considered a success.

**Technologies:** *Python3, FastAPI, Flagr, Locust, ElasticSearch, Redis, Amazon SQS, Amazon SNS, Splunk, Kubernetes,
Docker, AWS*

During my time at the company, I was promoted to Senior level and also received a salary increase.

### **Backend Developer** (Junior and Mid) - *QI Tech* (11/2019 - 01/2021)

I developed a service to offer SCR inquiries to the company's clients, control the authorizations of the consulted
people, and the number of inquiries made by clients in the month for billing purposes.

> The complexities of the project were: integrating with BACEN to make the inquiry; and ensuring that the inquiry could
> only be made if the consulted person digitally signed a document giving consent.
>
> The project involved: creating HTML document templates and populating them programmatically; integrating with the
> document generator service, the digital signature service, and with BACEN itself, sending requests and receiving
> webhooks; controlling the state of the entire process to give visibility to the client and to allow automation.
>
> In the end, the entire process was automated, another service could be offered by the company, and our clients
> obtained the necessary data to perform a good credit risk analysis in their funnels.

**Technologies:** *Python 3, Falcon, FastAPI, GCP, Google PubSub, Google Storage, MySQL, Kubernetes, Docker*

During my time at the company, I was recognized for high performance, and later received a salary increase.

### **Data Scientist** (Intern and Junior) - *brain4care* (03/2018 - 11/2019)

I developed several algorithms for acquisition, processing, and analysis of vital signs from patients of partner
hospitals.

> I built an auto-encoder neural network to reduce the dimensionality of time series of arterial pressure pulses,
> gold standard intra-cranial pressure, and non-invasive intra-cranial pressure. With this, we could extract features
> from the signals, cluster them, and even compare them in this lower dimensional space.
>
> I conducted statistical analyses for clinical studies conducted by the company in partnership with various researchers
> and hospitals, highlighting a reproducibility and repeatability study of the sensor for FDA approval and a study to
> check the hypothesis that signals from the non-invasive sensor could help identify individuals with type II diabetes
> mellitus.
>
> I created a REST API for visualization of captured vital signs, with the creation of an algorithm for data
> compression (reduction), preserving the waveforms of the signals.

**Technologies:** *Python 2, Flask, AWS, Keras, Tensorflow, Pandas, Scipy, SKLearn, Numpy*