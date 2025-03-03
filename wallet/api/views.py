from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from api.serializers import WalletSerializer
from api.models import Wallet


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    @action(detail=True, methods=['post'])
    def operation(self, request, pk=None):
        wallet = get_object_or_404(
            Wallet,
            pk=pk
        )
        operation_type = request.data.get('operation_type')
        amount = request.data.get('amount')

        if operation_type not in ['deposit', 'withdraw']:
            return Response(
                {'error': 'Неверный тип операции'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if operation_type == 'deposit':
            wallet.deposit(amount)
        elif operation_type == 'withdraw':
            wallet.withdraw(amount)

        return Response(
            {'balance': wallet.balance},
            status=status.HTTP_200_OK
        )
