from flask import Flask, jsonify, request
import random
app= Flask(__name__)
jokes = ["Why did the chicken cross the road? To get to the other side.","How many psychiatrists does it take to change a light bulb?None—the light bulb will change when it's ready.",
         "How many flies does it take to screw in a lightbulb? Two, but don't ask me how they got in there.", " How many hands does it take to change a lightbulb?Many."
         "What is black and white and red all over? A newspaper.","Why did the elephant paint its toenails red?So it could hide in a cherry tree.",
         "How can you tell that an elephant is in the bathtub with you?,By the smell of peanuts on its breath.","Why does an elephant have round flat feet? So that it can walk across lily pads." 
         "What is wool outside and cotton inside?A poodle in front of a drugstore with cotton swabs on sale.", "What is water around and the law in the middle?Judge Karapetyan in his pool."]
@app.route('/jokes/', methods=['GET'])
def getJokes():
    num = request.args.get("num",default=1,type=int)
    random_jokes =random.sample(jokes,num)
    return jsonify({"Jokes":random_jokes})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
