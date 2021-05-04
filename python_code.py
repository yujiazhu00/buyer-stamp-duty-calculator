def buyer_stamp_duty_calc(price):
    stage_1 = price - 180000
    if stage_1 <= 0:
        output_tax_1 = price * 0.01
        return output_tax_1
    if stage_1 > 0:
        stage_2 = stage_1 - 180000
        if stage_2 <= 0:
            output_tax_2 = 180000*0.01 + stage_1 * 0.02
            return output_tax_2
        if stage_2 > 0:
            stage_3 = stage_2 - 640000
            if stage_3 <= 0:
                output_tax_3 = 180000*0.01 + 180000*0.02 + stage_2 * 0.03
                return output_tax_3
            if stage_3 > 0:
                output_tax_4 = 180000*0.01 + 180000*0.02 + 640000 * 0.03 + stage_3 * 0.04
                return output_tax_4
