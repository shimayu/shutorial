def exgcd(m, n):
    if n == 0:
        assert m == 1
        return 1, 0
    else:
        x, y = exgcd(n, m % n)
        return y, x - m / n * y


if __name__ == '__main__':
    N = 386931010476066075837968435835568572278162262133897268076172926477773222237770106161904290022544637634198443777989318861346776496147456733417801969323559935547762053140311065149570645042679207282163944764258457818336874606186063312212223286995796662956880884390624903779609227558663952294861600483773641805524656787990883017538007871813015279849974842810524387541576499325580716200722985825884806159228713614036698970897017484020439048399276917685918470357385648137307211493845078192550112457897553375871556074252744253633037568961352527728436056302534978263323170336240030950585991108197098692769976160890567250487423 
### upper 512bit of p is calculated by sqrt(N) ### 
#    p = sqrt(N/19) 
    p = 142705255772364982838516531715718191640815441800236739365553038697417755590297275781522823491205105009501621401991866858062431379476890096993289842661379657285965454710848599435678159095824468488644765690029570153704491929476730805941135519670086613925329938990405788671905957539073166525554329183658867808814

### q is calculated by Coppersmith theorem. ###
#    q = 19 * p
#    PR.<x> = PolynomialRing(Zmod(N))
#    f = x + q
#    kbits = 512
#    x0 = f.small_roots(X=2^kbits, beta=0.3)[0]
#    q = x0 + q
    q = 2711399859674934673931814102598645641175493394204498047945507735250937356215648239848933646332896995180530806637845470303186196210060911842872507010566213492961135662215921968753949975482648800278196297048045096783128013026497367853790321266446269754792894427483593297724124126249179455165834403387544079388999
    
    p = N / q

    assert p * q == N

    e = 65537
    d, _ = exgcd(e, (p-1)*(q-1))
    d %= (p-1) * (q-1)

    C = 238128932536965734026453335534508678486770867304645614119195536048961186128744314667991999168452564298994773996973787655358503271491181214369796509942047091225518293577154563021214085132019889288510474458242494876257330038265066123460887568813277411779817556316602871932730284368524299559699693787556478631297630514938453794107136748994144175123917418701679413905695916367530746728699301383100433069740863537869450361306987480687067608102552418211244703552910903168179094472596152349098076535870469807035136435631458879919434041758274344589567529971195683495146426258135341109919085270442486183365562919531353370683625
    
    print(hex(pow(C, d, N))[2:-1].decode("hex"))
    
