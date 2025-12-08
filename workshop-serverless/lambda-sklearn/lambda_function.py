def predict_single(customer):
    # we will put our model here
    return 0.56

def lambda_handler(event, context):    
    print("Parameters:", event)
    customer = event['customer']
    prob = predict_single(customer)
    return {
        "churn_probability": prob,
        "churn": bool(prob >= 0.5)
    }