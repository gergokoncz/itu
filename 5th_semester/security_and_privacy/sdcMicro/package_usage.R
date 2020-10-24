# load library
library("sdcMicro")

# Set up dataset
data <- as.data.frame(cbind(as.factor(c('Urban', 'Urban', 'Urban', 'Urban', 'Rural', 'Urban', 'Urban', 'Urban',
                                        'Urban', 'Urban')),
                            as.factor(c('Female', 'Female', 'Female', 'Male',
                                        'Female', 'Male', 'Female', 'Male', 'Female', 'Female')),
                            as.factor(c('Sec in', 'Sec in', 'Prim in', 'Sec com', 'Sec com', 'Sec com', 'Prim com', 'Post-sec', 'Sec in', 'Sec in')),
                            as.factor(c('Emp', 'Emp', 'Non-LF', 'Emp', 'Unemp', 'Emp', 'Non-LF', 'Unemp', 'Non-LF','Non-LF')),
                            as.factor(c('yes', 'yes', 'yes', 'yes', 'yes', 'no', 'no', 'yes', 'no', 'yes')),
                            c(180, 180, 215, 76, 186, 76, 180, 215, 186, 76)
))

# Specify variable names
names(data) <- c('Residence', 'Gender', 'Educ', 'Lstat', 'Health', 'Weights')

# Set up sdcMicro object with specified quasi-identifiers and weight variable
sdcInitial <- createSdcObj(dat = data, keyVars = c('Residence', 'Gender', 'Educ', 'Lstat'), weightVar = 'Weights')

freq(sdcInitial, type = "fk")

sdcInitial@risk$individual

# sdc create object examples
showClass("sdcMicroObj")

data("testdata")
sdc <- createSdcObj(testdata,
                    keyVars=c('urbrur','roof','walls','water','electcon','relat','sex'),
                    numVars=c('expend','income','savings'), w='sampling_weight')
head(sdc@manipNumVars)

# display risks
sdc@risk$global
sdc <- dRisk(sdc)
sdc@risk$numeric

sdc <- addNoise(sdc,variables=c("expend","income"))

sdc <- undolast(sdc)

sdc <- addNoise(sdc, noise=0.2)
head(sdc@manipNumVars)
sdc@risk$numeric

head(sdc@risk$individual)
sdc@risk$global

sdc <- dataGen(sdc)

##microaggregation

head(get.sdcMicroObj(sdc, type="manipNumVars"))
sdc <- microaggregation(sdc)

## pram
sdc <- pram(sdc,keyVar="water")