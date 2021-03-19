Regression Project: Estimating Home Value
Scenario
You are a junior data scientist on the Zillow data science team and recieve the following email in your inbox:

We want to be able to predict the values of single unit properties that the tax district assesses using the property data from those with a transaction during the "hot months" (in terms of real estate demand) of May-August, 2017.

We also need some additional information outside of the model.

Zach lost the email that told us where these properties were located. Ugh, Zach :-/. Because property taxes are assessed at the county level, we would like to know what states and counties these are located in.

We'd also like to know the distribution of tax rates for each county.

The data should have the tax amounts and tax value of the home, so it shouldn't be too hard to calculate. Please include in your report to us the distribution of tax rates for each county so that we can see how much they vary within the properties in the county and the rates the bulk of the properties sit around.

Note that this is separate from the model you will build, because if you use tax amount in your model, you would be using a future data point to predict a future data point, and that is cheating! In other words, for prediction purposes, we won't know tax amount until we know tax value.

-- The Zillow Data Science Team

Specification
Audience
Your customer/end user is the Zillow data science team. In your deliverables, be sure to re-state your goals, as if you were delivering this to Zillow. They have asked for something from you, and you are basically communicating in a more concise way, and very clearly, the goals as you understand them and as you have taken and acted upon them through your research.

Deliverables
Remember that you are communicating to the Zillow team, not to your instructors. So, what does the team expect to receive from you?

See the Pipeline guidance below for more information on expectations within these deliverables.

A report in the form of a presentation, verbal supported by slides.

The report/presentation slides should summarize your findings about the drivers of the single unit property values. This will come from the analysis you do during the exploration phase of the pipeline. In the report, you should have visualizations that support your main points.

The presentation should be no longer than 5 minutes.

A github repository containing your work.

This repository should contain one clearly labeled final Jupyter Notebook that walks through the pipeline, but, if you wish, you may split your work among 2 notebooks, one for exploration and one for modeling. In exploration, you should perform your analysis including the use of at least two statistical tests along with visualizations documenting hypotheses and takeaways. In modeling, you should establish a baseline that you attempt to beat with various algorithms and/or hyperparameters. Evaluate your model by computing the metrics and comparing.

Make sure your notebook answers all the questions posed in the email from the Zillow data science team.

The repository should also contain the .py files necessary to reproduce your work, and your work must be reproducible by someone with their own env.py file.

As with every project you do, you should have an excellent README.md file documenting your project planning with instructions on how someone could clone and reproduce your project on their own machine. Include at least your goals for the project, a data dictionary, and key findings and takeaways. Your code should be well documented.

Project Guidance
you will need to reference the properties_2017 and predictions_2017 tables.

For the first iteration of your model, use only square feet of the home, number of bedrooms, and number of bathrooms to estimate the property's assessed value, taxvaluedollarcnt. You can expand this to other fields after you have completed an mvp (minimally viable product).

You will need to figure out which field gives you the annual tax amount for the property in order to calculate the tax rate. Using the property's assessed value (taxvaluedollarcnt) and the amount they pay each year (<field name>) to compute tax rate.

You will want to read and re-read the requirements given by your stakeholders to be sure you are meeting all of their needs and representing it in your data, report, and model.

You will want to do some data validation or QA (quality assurance) to be sure the data you gather is what you think it is.

You will want to make sure you are using the best fields to represent square feet of home, number of bedrooms, and number of bathrooms. "Best" meaning the most accurate and available information. Here you will need to do some data investigation in the database and use your domain expertise to make some judgement calls.

Data Science Pipeline Guidance
Project Planning
Goal: leave this section with (at least the outline of) a plan for the project documented in your README.md file.

Think about the following in this stage:

Brainstorming ideas and form hypotheses related to how variables might impact or relate to each other, both within independent variables and between the independent variables and dependent variable.

Document any ideas for new features you may have while first looking at the existing variables and the project goals ahead of you.

Think about what things in your project are nice to have, versus which things are need to have. For example, you might document that you will only worry about trying to scale your features after creating and evaluating a baseline model.

Acquire
Goal: leave this section with a dataframe ready to prepare.

Think about the following in this stage:

The ad hoc part includes summarizing your data as you read it in and begin to explore, look at the first few rows, data types, summary stats, column names, shape of the data frame, etc.

Create an acquire.py file the reproducible component for gathering data from a database using SQL and reading it into a pandas DataFrame.

Prep
Goal: leave this section with a dataset that is split into train, validate, and test ready to be analyzed. Make sure data types are appropriate and missing values have been addressed, as have any data integrity issues.

Think about the following in this stage:

This might include plotting the distributions of individual variables and using those plots to identify and decide how best to handle any outliers.

You might also identify unit measures to decide how best to scale any numeric data as you see necessary.

Identify erroneous or invalid data that may exist in your dataframe.

Add a data dictionary in your notebook at this point that defines all the fields used in your model and your analysis and answers the question, "Why did you use the fields you used?". e.g. "Why did you use bedroom_field1 over bedroom_field2?", not, "Why did you use number of bedrooms?"

Create a prep.pyfile as the reproducible component that handles missing values, fixes data integrity issues, changes data types, scales data, etc.

Data Exploration
Goal: I recommend following the exploration approach of univariate, bivariate, multivariate discussed in class. In that method, you can address each of the questions you posed in your planning and brainstorming and any others you have come up with along the way through visual exploration and statistical analysis. The findings from your analysis should provide you with answers to the specific questions your customer asked that will be used in your final report as well as information to move forward toward building a model.

Think about the following in this stage:

Run at least 1 t-test and 1 correlation test (but as many as you need!)

Visualize all combinations of variables in some way(s).

What independent variables are correlated with the dependent?

Which independent variables are correlated with other independent variables?

Make sure to summarize your takeaways and conclusions. That is, the Zillow data science team doesn't want to see just a bunch of dataframes, numbers, and charts without any explanation; you should explain in the notebook what these mean, interpret them.

Modeling
Goal: develop a regression model that performs better than a baseline.

Think about the following in this stage:

Extablishing and evaluating a baseline model and showing how the model you end up with performs better.

Documenting various algorithms and/or hyperparameters you tried along with the evaluation code and results in your notebook before settling on the best algorithm.

Evaluating your model using the standard techniques: plotting the residuals, computing the evaluation metrics (SSE, RMSE, and/or MSE), comparing to baseline, plotting 
y
 by 
^
y
.

For some additional options see sklearn's linear models and sklearn's page on supervised learning.

After developing a baseline model, you could do some feature engineering and answer questions like:

Which features should be included in your model?

Are there new features you could create based on existing features that might be helpful?

Are there any features that aren't adding much value?

Here you could also use automated feature selection techniques to determine which features to put into your model.

You should make sure that any transformation that you apply to your training dataframe are reproducible, that is, the same transformations can be applied to your test dataset.