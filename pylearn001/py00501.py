#-*-coding:utf-8-*-
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
cheight = 2.5*height #����
weight = 180 # lbs
cweight = 0.45*weight #ǧ��
eyes = 'Blue'
teeth = "White"
hair = "Brown"


print "Ler's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "if I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "print anything %r,%r,%r,%r." % (name,height,weight,eyes)

print "print anything name %r,cheight %r ����,cweight %r ǧ��, eyes %r��" % (name,cheight,cweight,eyes)
