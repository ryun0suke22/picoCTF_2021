def decode(str):
    ans = str[0:8] + str[15:7:-1]
    for i in range(16, 31, 2):
        ans += str[46-i] + str[i+1]
    print(ans)
    return ans

test="jU5t_a_sna_3lpm18g947_u_4_m9r54f"
print(test)
plain=decode(test)
decode(plain)
