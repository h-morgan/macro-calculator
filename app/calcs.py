
def calculate(form):
  results = {}
  gender = form.gender.data

  # first convert weight from lbs to kg and height to cm 
  weight_kg = form.weight.data / 2.20462
  height_cm = ((form.height_ft.data * 12) + form.height_in.data) * 2.54
  
  # calculate BMR 
  if gender == 'male':
    bmr = (10*weight_kg) + (6.25*height_cm) - (5*form.age.data) + 5
  if gender == 'female':
    bmr = (10*weight_kg) + (6.25*height_cm) - (5*form.age.data) - 161
  results['bmr'] = round(bmr)

  # next calculate total caloric expenditure using activity level & BMR
  tce_multiplier = {'sedentary' : 1.2, 'light' : 1.375, 'moderate' : 1.55, 'very' : 1.725, 'extra' : 1.9 }
  tce = round(bmr * tce_multiplier[form.activity_level.data])
  results['tce'] = tce
  
  # find caloric target amount  using client's goal 
  goal_adjust = {'lose' : -400, 'gain' : 400, 'maintain' : 0 }
  caloric_target = tce + goal_adjust[form.fitness_goal.data]
  results['target_cals'] = caloric_target

  # divide caloric target by body type % values 
  body_type_adjust = {}
  body_type_adjust['ectomorph'] = {'protein' : 0.25, 'carbs' : 0.55, 'fat' : 0.20 }
  body_type_adjust['mesomorph'] = {'protein' : 0.30, 'carbs' : 0.40, 'fat' : 0.30 }
  body_type_adjust['endomorph'] = {'protein' : 0.35, 'carbs' : 0.25, 'fat' : 0.40 }
  results['calorie_percents'] = body_type_adjust[form.body_type.data]

  # get % of calories of each macro into grams
  cals_protein = round(caloric_target * body_type_adjust[form.body_type.data]['protein'])
  cals_carbs = round(caloric_target * body_type_adjust[form.body_type.data]['carbs'])
  cals_fat = round(caloric_target * body_type_adjust[form.body_type.data]['fat'])
  results['cals'] = {'protein' : cals_protein, 'fat' : cals_fat, 'carbs' : cals_carbs }
  
  grams_protein = round(cals_protein / 4)
  grams_fat = round(cals_fat / 9)
  grams_carbs = round(cals_carbs / 4)
  results['grams'] = {'protein' : grams_protein, 'carbs' : grams_carbs, 'fat' : grams_fat }
    

  return results
