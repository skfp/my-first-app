from learning_app.models import Card,User,Answer

import sys

def add_answer():
    NewAnswerRecord = ( answer_id=1,
    card_id_ans=1,
    pile_id=1,
    answer="E"
    )
    NewAnswerRecord.save()
    print("poop")


if __name__ == "__main__":
    add_answer()