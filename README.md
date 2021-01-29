# King County House Sales Linear Regression Model

![editorial cartoon of couple house hunting in seattle looking at the affordable dog house, by David Horsey in the Seattle Times](/images/Dog-house.jpg)

### Business Problem

Seattle is the fastest growing city in the country with a population increase of almost 30% from 2010 to 2020. The surrounding King County ranks 3rd in the country for growth with a population increase of 16% in the same timeframe. All this growth has increased demand for housing and caused home prices to skyrocket. The median house price in Seattle rose 93% from 2012-2018.

This is a difficult market for home buyers, so this project will help buyers decide what trade-offs are worthwhile to find the best house for their needs in their price range.

### Method

I used Scikit Learn to build a multilinnear regression model to predict house prices using the King County House Sales dataset. I also used a dataset of King County zipcodes and median incomes from Communities Count- a King County population dashboard to investigate the roll of median household income on the effect of zipcodes in determining house prices.

### Results

In building this model, I determined that zipcode is the most important feature in determining a the price of a home. If you would like to have Bill Gates and Jeff Bezos as neighbors, you can expect to pay 135% more for home, compared to similar homes in the mean neighborhoods. Suburbs to the south of Seattle offer have prices 30% lower than similar homes in the mean neighborhoods. 

After zipcode, the square footage of a home the next largest impact on home price, with the above ground space having a much larger impact on home price than basement size. Additionally, it seems that any price difference that comes from additional bedrooms is due to the increase in size, not the number of bedrooms.

<img src="images/increasebysqft.png" alt="graph of change in house price with increasing house size" width="1000"/>

Finally, the number of bathrooms can significantly increase home prices, especially in the jump from 1 to 2 bathrooms.

<img src="images/increasebybathroom.png" alt="graph of change in house price with more bathrooms" width="500"/>

### Conclusions

This model can account for 85% of the variability in house prices in King County. I think the model is a decent start, but could be improved by doing more to work out the best transformation method for each feature. Additionally, I would like to try different scaling methods. 

Zipcode has an outsized effect on the model, so I would like to explore other aspects of zipcode to see what might contribute to the effect. Perhaps building a model for each zipcode would be a way to keep the zipcode from having too much influence on the model.

Seattle's population growth and corresponding demand for housing has lead to a change in zoning laws that allow "Accesory Dwelling Units" to be built on lots already having a main house. It would be interesting to see how these additional units will impact the value of homes with and without them. It seems like additional space would increase value, but perhaps the exclusivity factor of having a private yard will also play a role in pricing. 

The next step for this model is to build out an application that will allow buyers to use sliders to change house features- location, bathrooms, square footage, etc- and see the effect those changes have on house price.

This analysis would benefit from more recent data and as well as the previously mentioned more fine tuning of the data. Overall, it does a decent job of predicting house prices in King County in the years 2014 & 2015.

