from formater import *
import json


def BuyParserVIP(text):

    data = {}

    lines = text.split("\n")
    data["name"] = lines[0].split()[2]
    data["leverage"] = lines[0].split()[5]
    data["entry"] = lines[2].split(":")[1][1:]
    data["targets"] = lines[4].split(":")[1][1:]
    data["stop_loss"] = lines[6].split(":")[1][1:]

    json_data = json.dumps(data, indent=4)
    return BuyFormaterVIP(data)

def SellParserVIP(text):

    data = {}

    lines = text.split("\n")
    data["name"] = lines[0].split()[3]
    data["leverage"] = lines[0].split()[6]
    data["entry"] = lines[2].split(":")[1][1:]
    data["targets"] = lines[4].split(":")[1][1:]
    data["stop_loss"] = lines[6].split(":")[1][1:]

    json_data = json.dumps(data, indent=4)

    return SellFormaterVIP(data)


def TargetParser(text):
    data = {}

    lines = text.split("\n")
    data["name"] = lines[0].split()[0]
    data["profit"] = lines[1].split(":")[1][1:]
    data["period"] = lines[2].split(":")[1][1:]

    json_data = json.dumps(data, indent=4)
    return TargetFormater(data)



def LossParser(text):
    data = {}
    lines = text.split("\n")
    data["name"] = lines[0].split()[0]
    data["loss"] = lines[1].split(":")[1][1:]

    json_data = json.dumps(data, indent=4)
    # print(json_data)
    return LossFormater(data)


def AllTargetsParser(text):
    data = {}
    lines = text.split("\n")
    data["name"] = lines[0].split()[0]
    data["profit"] = lines[1].split(":")[1][1:]
    data["period"] = lines[2].split(":")[1][1:]
    json_data = json.dumps(data, indent=4)
    return AllTargetsFormater(data)


def MessageParserVIP(text):
    try:
        lines = text.split("\n")
        if lines[0].split()[0] == "Buy":
            return BuyParserVIP(text)
        if lines[0].split()[1] == "Sell":
            return SellParserVIP(text)
        if lines[0].split()[2] == "Target":
            return TargetParser(text)
        if lines[0].split()[2] == "Stop":
            return LossParser(text)
        if lines[0].split()[1] == "All":
            return AllTargetsParser(text)
        return "Error"
    except:
        return "Error"

def MessageParser(text):
    try:
        lines = text.split("\n")
        if lines[0].split()[0] == "Buy":
            return BuyParser(text)
        if lines[0].split()[1] == "Sell":
            return SellParser(text)
        if lines[0].split()[2] == "Target":
            return TargetParser(text)
        if lines[0].split()[2] == "Stop":
            return LossParser(text)
        if lines[0].split()[1] == "All":
            return AllTargetsParser(text)
        return "Error"
    except:
        return "Error"


def BuyParser(text):

    data = {}

    lines = text.split("\n")
    data["name"] = lines[0].split()[2]
    data["leverage"] = lines[0].split()[5]
    data["entry"] = lines[2].split(":")[1][1:]
    data["targets"] = lines[4].split(":")[1][1:]
    data["stop_loss"] = lines[6].split(":")[1][1:]

    json_data = json.dumps(data, indent=4)
    return BuyFormaterVIP(data)

def SellParser(text):

    data = {}

    lines = text.split("\n")
    data["name"] = lines[0].split()[3]
    data["leverage"] = lines[0].split()[6]
    data["entry"] = lines[2].split(":")[1][1:]
    data["targets"] = lines[4].split(":")[1][1:]
    data["stop_loss"] = lines[6].split(":")[1][1:]

    json_data = json.dumps(data, indent=4)

    return SellFormaterVIP(data)



# text = """#DOGEUSDT All take-profit targets achieved
# 🎯 Profit: 61.9057%
# ⏰ Period: 1 Days 0 Hours 25 Minutes"""
#
# print(MessageParser(text))