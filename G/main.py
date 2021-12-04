import spacy


def spacy_commands():
    while True:
        output = {}
        pos = []
        command = input("\nEnter command: ")
        doc = nlp(command)

        if spacy.explain(doc[0].tag_) == "verb, base form":
            output["action"] = doc[0].text
            pos.append({doc[0]: doc[0].pos_})

            obj = []
            for i in range(1, len(doc)):
                print(i)
                # print(doc[i], ':', spacy.explain(doc[i].pos_), ',', spacy.explain(doc[i].tag_))
                pos.append({doc[i]: doc[i].pos_})
                obj.append(doc[i].text)
                output["object"] = " ".join(obj)
                if doc[i].pos_ == "NOUN":
                    if len(doc) == i + 1:
                        break
                    elif doc[i + 1].pos_ != "NOUN":
                        break

            print(output)
            print(pos)
        else:
            break


if __name__ == "__main__":
    nlp = spacy.load("en_core_web_sm")
    spacy_commands()
