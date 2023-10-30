import pandas


def get_fund_name(video_data_list):
    filtered_dict = {
        "Multimercado": [],
        "Renda Fixa": [],
        "Credito Privado": [],
        "Acoes": [],
        "CRIs": [],
        "KNRI11": [],
        "KFOF11": [],
        "KEVE11": [],
        "Others": []
    }

    for video_data in video_data_list:
        if not video_data:
            break

        title_prefix = video_data.get("Title").split('-')[0]

        if "Multimercado" in title_prefix:
            filtered_dict["Multimercado"].append(video_data)

        elif "Renda Fixa" in title_prefix:
            filtered_dict["Renda Fixa"].append(video_data)

        elif "Crédito Privado" in title_prefix:
            filtered_dict["Credito Privado"].append(video_data)

        elif "Ações" in title_prefix:
            filtered_dict["Acoes"].append(video_data)

        elif "CRIs" in title_prefix:
            filtered_dict["CRIs"].append(video_data)

        elif "KNRI11" in title_prefix:
            filtered_dict["KNRI11"].append(video_data)

        elif "KFOF11" in title_prefix:
            filtered_dict["KFOF11"].append(video_data)

        elif "KEVE11" in title_prefix:
            filtered_dict["KEVE11"].append(video_data)

        else:
            filtered_dict["Others"].append(video_data)

    return filtered_dict


def order_by_publish_date(filtered_dict):
    for fund in filtered_dict:
        sorted_list = sorted(filtered_dict.get(fund), key=lambda x: x["Published At"], reverse=True)
        filtered_dict[fund] = sorted_list

    return filtered_dict





